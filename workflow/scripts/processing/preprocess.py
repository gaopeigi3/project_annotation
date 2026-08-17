import argparse
import scanpy as sc

from scrna_pipeline.preprocess import clean_genes, run_preprocess


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--n-hvg", type=int, required=True)
    parser.add_argument("--min-cells", type=int, required=True)
    parser.add_argument("--remove-mt", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--remove-ribo", action=argparse.BooleanOptionalAction, default=True)

    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)

    adata = clean_genes(
        adata,
        remove_mt=args.remove_mt,
        remove_ribo=args.remove_ribo,
    )

    adata = run_preprocess(
        adata,
        n_hvg=args.n_hvg,
        min_cells=args.min_cells,
    )

    adata.write(args.output)


if __name__ == "__main__":
    main()