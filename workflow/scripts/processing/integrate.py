# workflow/scripts/processing/integrate.py

import argparse
import scanpy as sc

from scrna_pipeline.integrate import run_integration


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--method", required=True)
    parser.add_argument("--key", required=True)

    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)

    adata = run_integration(
        adata,
        method=args.method,
        key=args.key,
    )

    adata.write(args.output)


if __name__ == "__main__":
    main()