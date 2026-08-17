REQUIRED_INPUT_OBS = ("sample", "batch")
REQUIRED_OUTPUT_OBS = ("celltype", "celltype_confidence", "annotation_source", "annotation_version")
REQUIRED_OUTPUT_UNS = ("celltype_colors", "annotation_metadata")


def validate_input(adata):
    missing = [name for name in REQUIRED_INPUT_OBS if name not in adata.obs]
    if missing:
        raise ValueError(f"Missing required obs columns: {', '.join(missing)}")
    if adata.n_obs == 0 or adata.n_vars == 0:
        raise ValueError("Input AnnData must contain cells and genes")
    return adata


def validate_output(adata):
    missing_obs = [name for name in REQUIRED_OUTPUT_OBS if name not in adata.obs]
    missing_uns = [name for name in REQUIRED_OUTPUT_UNS if name not in adata.uns]
    if missing_obs or missing_uns:
        raise ValueError(f"Invalid annotated AnnData; missing obs={missing_obs}, uns={missing_uns}")
    return adata
