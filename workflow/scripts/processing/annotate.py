# rank_genes_groups
from .lymphoid import lymphoid_schema
from .myeloid import myeloid_schema
from .erythroid import erythroid_schema
from .progenitor import progenitor_schema

celltype_schema = {
    **lymphoid_schema,
    **myeloid_schema,
    **erythroid_schema,
    **progenitor_schema,
}


def score_lineages(
    cluster_expr,
    marker_schema
):
    scores = {}

    for lineage, info in marker_schema.items():

        markers = info["general"]

        valid = get_valid_markers(
            markers,
            cluster_expr.index
        )

        if not valid:
            continue

        scores[lineage] = cluster_expr[valid].mean()

    return scores