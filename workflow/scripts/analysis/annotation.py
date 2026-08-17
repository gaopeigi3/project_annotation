import argparse
import scanpy as sc

from scrna_pipeline.annotation import (
    annotate_by_marker_voting,
    apply_celltype_colors,
    celltype_colors_dict,
)

from scrna_pipeline.markers_all import hierarchical_markers


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--scores", required=True)

    parser.add_argument(
        "--threshold-main",
        type=float,
        required=True,
    )

    parser.add_argument(
        "--threshold-sub",
        type=float,
        required=True,
    )

    args = parser.parse_args()

    # 1. read
    adata = sc.read_h5ad(args.input)

    # 2. annotation
    adata, cluster_map, score_df = annotate_by_marker_voting(
        adata,
        hierarchical_markers,
        threshold_main=args.threshold_main,
        threshold_sub=args.threshold_sub,
    )

    # 3. colors
    adata = apply_celltype_colors(
        adata,
        celltype_colors_dict,
    )

    # 4. write artifacts
    adata.write(args.output)
    score_df.to_csv(args.scores, index=False)


if __name__ == "__main__":
    main()