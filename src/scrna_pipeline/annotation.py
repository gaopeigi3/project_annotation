import numpy as np
import pandas as pd


def _score_markers(adata, markers):
    marker_names = list(dict.fromkeys(markers))
    available = [gene for gene in marker_names if gene in adata.var_names]
    if not available or not marker_names:
        return 0.0, len(available), len(marker_names)
    values = np.asarray((adata[:, available].X > 0).mean(axis=0)).ravel()
    score = float(values.mean()) * len(available) / len(marker_names)
    return score, len(available), len(marker_names)


def _subtypes(definition):
    result = {}
    for module in definition.get("modules", {}).values():
        if module.get("enabled_by_default", False):
            result.update(module.get("subtypes", {}))
    return result


def annotate_by_marker_voting(
    adata,
    marker_schema,
    threshold_main=0.3,
    threshold_sub=0.4,
):
    if "leiden" not in adata.obs:
        raise KeyError("'leiden' not found in adata.obs")
    if not marker_schema:
        raise ValueError("No marker schema was provided")

    expression = adata.raw.to_adata() if adata.raw is not None else adata
    cluster_map = {}
    confidence_map = {}
    score_records = []

    for cluster in adata.obs["leiden"].astype(str).unique():
        cell_mask = adata.obs["leiden"].astype(str) == cluster
        cluster_adata = expression[cell_mask]
        main_scores = {}

        for celltype, definition in marker_schema.items():
            markers = definition.get("markers", {}).get("general", [])
            score, available, total = _score_markers(cluster_adata, markers)
            main_scores[celltype] = score
            score_records.append({
                "cluster": cluster,
                "level": "main",
                "celltype": celltype,
                "score": score,
                "available_markers": available,
                "total_markers": total,
            })

        best_celltype = max(main_scores, key=main_scores.get)
        best_score = main_scores[best_celltype]
        annotation = "Unknown"

        if best_score >= threshold_main:
            annotation = best_celltype
            subtype_scores = {}
            for subtype, definition in _subtypes(marker_schema[best_celltype]).items():
                score, available, total = _score_markers(
                    cluster_adata, definition.get("markers", [])
                )
                subtype_scores[subtype] = score
                score_records.append({
                    "cluster": cluster,
                    "level": "subtype",
                    "celltype": subtype,
                    "score": score,
                    "available_markers": available,
                    "total_markers": total,
                })
            if subtype_scores:
                best_subtype = max(subtype_scores, key=subtype_scores.get)
                if subtype_scores[best_subtype] >= threshold_sub:
                    annotation = best_subtype
                    best_score = subtype_scores[best_subtype]

        cluster_map[cluster] = annotation
        confidence_map[cluster] = best_score
        for record in score_records:
            if record["cluster"] == cluster:
                record["annotation"] = annotation

    leiden = adata.obs["leiden"].astype(str)
    adata.obs["celltype"] = leiden.map(cluster_map).astype("category")
    adata.obs["celltype_confidence"] = leiden.map(confidence_map).astype(float)
    return adata, cluster_map, pd.DataFrame(score_records)


def apply_annotation_metadata(adata, source="marker_voting", version="0.1.0"):
    adata.obs["annotation_source"] = source
    adata.obs["annotation_version"] = version
    adata.uns["annotation_metadata"] = {
        "source": source,
        "version": version,
    }
    return adata


def apply_celltype_colors(adata, colors):
    if "celltype" not in adata.obs:
        raise KeyError("'celltype' not found in adata.obs")
    categories = adata.obs["celltype"].cat.categories
    adata.uns["celltype_colors"] = [
        colors.get(category, "#999999") for category in categories
    ]
    return adata
