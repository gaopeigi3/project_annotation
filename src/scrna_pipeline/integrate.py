# src/scrna_pipeline/integrate.py

import scanpy as sc
import scanpy.external as sce


def run_integration(
    adata,
    method="harmony",
    key="sample",
    n_pcs=50,
):
    if key not in adata.obs:
        raise KeyError(f"Integration key '{key}' not found in adata.obs")
    n_comps = min(n_pcs, adata.n_obs - 1, adata.n_vars - 1)
    if n_comps < 2:
        raise ValueError("Integration requires at least 3 cells and 3 genes")

    sc.pp.scale(adata, max_value=10)

    sc.tl.pca(
        adata,
        svd_solver="arpack",
        n_comps=n_comps,
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