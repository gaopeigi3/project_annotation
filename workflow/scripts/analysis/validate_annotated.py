import argparse

import scanpy as sc

from scrna_pipeline.validation import validate_output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    validate_output(sc.read_h5ad(args.input))


if __name__ == "__main__":
    main()
