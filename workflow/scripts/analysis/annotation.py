import argparse

import scanpy as sc

from config.schema.color import celltype_colors_dict
from config.schema.erythroid import erythroid_schema
from config.schema.lymphoid import lymphoid_schema
from config.schema.myeloid import myeloid_schema
from config.schema.progenitor import progenitor_schema
from scrna_pipeline.validation import validate_output
from scrna_pipeline.annotation import (
    annotate_by_marker_voting,
    apply_annotation_metadata,
    apply_celltype_colors,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--scores", required=True)
    parser.add_argument("--threshold-main", type=float, required=True)
    parser.add_argument("--threshold-sub", type=float, required=True)
    parser.add_argument("--version", default="0.1.0")
    args = parser.parse_args()

    marker_schema = {}
    for schema in (
        erythroid_schema,
        lymphoid_schema,
        myeloid_schema,
        progenitor_schema,
    ):
        overlap = marker_schema.keys() & schema.keys()
        if overlap:
            raise ValueError(f"Duplicate cell types in marker schemas: {sorted(overlap)}")
        marker_schema.update(schema)

    adata = sc.read_h5ad(args.input)
    adata, _, score_df = annotate_by_marker_voting(
        adata,
        marker_schema,
        threshold_main=args.threshold_main,
        threshold_sub=args.threshold_sub,
    )
    colors = {
        name: definition.get("color", celltype_colors_dict.get(name, "#999999"))
        for name, definition in marker_schema.items()
    }
    colors.update(celltype_colors_dict)
    adata = apply_celltype_colors(adata, colors)
    adata = apply_annotation_metadata(adata, version=args.version)
    validate_output(adata)
    adata.write(args.output)
    score_df.to_csv(args.scores, index=False)


if __name__ == "__main__":
    main()
