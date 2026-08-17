import scanpy as sc


def run_reduction(
    adata,
    n_neighbors=15,
    resolution=0.8,
    use_rep=None,
):
    sc.pp.neighbors(
        adata,
        n_neighbors=n_neighbors,
        use_rep=use_rep,
    )

    sc.tl.umap(adata)

    sc.tl.leiden(
        adata,
        resolution=resolution,
    )

    return adata