# workflow/scripts/visualization/visualize.py

import argparse
import scanpy as sc

from scrna_pipeline.visualize import plot_umap


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--umap-celltype", required=True)
    parser.add_argument("--umap-sample", required=True)

    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)

    plot_umap(
        adata,
        color="celltype",
        output=args.umap_celltype,
        title="Cell type",
    )

    plot_umap(
        adata,
        color="sample",
        output=args.umap_sample,
        title="Sample",
    )


if __name__ == "__main__":
    main()