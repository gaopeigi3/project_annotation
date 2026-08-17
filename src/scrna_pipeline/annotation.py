# src/scrna_pipeline/annotation.py

import pandas as pd


def annotate_by_marker_voting(
    adata,
    hierarchical_markers,
    threshold_main=0.3,
    threshold_sub=0.4,
):
    cluster_map = {}
    score_records = []

    clusters = adata.obs["leiden"].astype(str).unique()

    for cluster in clusters:
        cluster_adata = adata[adata.obs["leiden"].astype(str) == cluster]

        # --------------------------------------------------
        # 1. 对这个 cluster 计算各 cell type marker score
        # --------------------------------------------------
        scores = {}

        for celltype, markers in hierarchical_markers.items():
            available_markers = [
                gene
                for gene in markers
                if gene in cluster_adata.var_names
            ]

            if not available_markers:
                scores[celltype] = 0.0
                continue

            # 这里放你原来 marker voting 的真实计算逻辑
            score = ...
            scores[celltype] = score

        # --------------------------------------------------
        # 2. 根据 score 决定 annotation
        # --------------------------------------------------
        best_celltype = max(scores, key=scores.get)
        best_score = scores[best_celltype]

        if best_score >= threshold_main:
            annotation = best_celltype
        else:
            annotation = "Unknown"

        cluster_map[cluster] = annotation

        # --------------------------------------------------
        # 3. 保存 score，方便检查 annotation provenance
        # --------------------------------------------------
        for celltype, score in scores.items():
            score_records.append(
                {
                    "cluster": cluster,
                    "celltype": celltype,
                    "score": score,
                    "annotation": annotation,
                }
            )

    # ------------------------------------------------------
    # 4. cluster annotation 映射回每个 cell
    # ------------------------------------------------------
    adata.obs["celltype"] = (
        adata.obs["leiden"]
        .astype(str)
        .map(cluster_map)
        .astype("category")
    )

    score_df = pd.DataFrame(score_records)

    return adata, cluster_map, score_df