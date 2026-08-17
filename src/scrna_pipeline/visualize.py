import matplotlib.pyplot as plt
import scanpy as sc


def plot_umap(
    adata,
    color,
    output,
    title=None,
):
    sc.pl.umap(
        adata,
        color=color,
        title=title,
        show=False,
    )

    plt.savefig(
        output,
        bbox_inches="tight",
        dpi=300,
    )

    plt.close()