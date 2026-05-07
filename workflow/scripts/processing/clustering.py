# leiden / resolution

def run_harmony(
    adata,
    batch_key="patient",
    basis="X_scVI"
):
    sce.pp.harmony_integrate(
        adata,
        key=batch_key,
        basis=basis
    )

    return adata



    sc.pp.neighbors(adata_filter, use_rep=f'X_harmony', n_neighbors=n_neighbors)
    sc.tl.leiden(adata_filter, resolution=resolution)