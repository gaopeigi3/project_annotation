import argparse
import scanpy as sc
from scrna_pipeline.qc import run_qc


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        required=True,
    )

    parser.add_argument(
        "--output",
        required=True,
    )

    parser.add_argument(
        "--min-genes",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--max-mt",
        type=float,
        required=True,
    )

    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)

    adata = run_qc(
        adata,
        min_genes=args.min_genes,
        max_mt=args.max_mt,
    )

    adata.write(args.output)


if __name__ == "__main__":
    main()