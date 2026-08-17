# src/scrna_pipeline/integrate.py

import scanpy as sc
import scanpy.external as sce


def run_integration(
    adata,
    method="harmony",
    key="sample",
):
    sc.pp.scale(adata, max_value=10)

    sc.tl.pca(
        adata,
        svd_solver="arpack",
        n_comps=50,
        use_highly_variable=True,
    )

    if method == "harmony":
        sce.pp.harmony_integrate(
            adata,
            key=key,
        )

    elif method == "none":
        pass

    else:
        raise ValueError(
            f"Unknown integration method: {method}"
        )

    return adata