import argparse

import scanpy as sc

from scrna_pipeline.reduce import run_reduction


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--n-neighbors", type=int, required=True)
    parser.add_argument("--resolution", type=float, required=True)
    parser.add_argument("--method", choices=("harmony", "none"), required=True)
    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)
    use_rep = "X_pca_harmony" if args.method == "harmony" else "X_pca"
    if use_rep not in adata.obsm:
        raise KeyError(f"Representation '{use_rep}' not found in adata.obsm")
    adata = run_reduction(adata, args.n_neighbors, args.resolution, use_rep)
    adata.write(args.output)


if __name__ == "__main__":
    main()
