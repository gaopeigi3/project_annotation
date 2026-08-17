import argparse
import json
import scanpy as sc
from scrna_pipeline.validation import validate_input

from scrna_pipeline.cohort import select_cohort


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--filters", required=True)

    args = parser.parse_args()

    filters = json.loads(args.filters)

    adata = validate_input(sc.read_h5ad(args.input))

    adata = select_cohort(
        adata,
        filters=filters,
    )

    adata.write(args.output)


if __name__ == "__main__":
    main()