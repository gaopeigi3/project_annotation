# project_annotation

A two-layer, reproducible single-cell annotation pipeline.

## Infrastructure

- Layer 1 — scientific calculation: Scanpy and testable Python functions in `src/scrna_pipeline/`.
- Layer 2 — workflow: Snakemake rules in `workflow/`.

Service and container layers are intentionally out of scope.

## Data contract

Input is an AnnData `.h5ad` file with required `obs` columns `sample` and `batch`.
Optional cohort columns are configured in `config/config.yaml`.

The annotated output contains:

- `obs`: `celltype`, `celltype_confidence`, `annotation_source`, and `annotation_version`.
- `uns`: `celltype_colors` and `annotation_metadata`.

## Workflow

`input.h5ad → cohort → QC → preprocess → integrate → reduce/cluster → annotate → visualize`

## Setup and run

```bash
python -m pip install -e '.[workflow]'
snakemake --software-deployment-method conda --cores 1
```

Place the input at `data/raw/input.h5ad`, or change `data.input_h5ad` in
`config/config.yaml`. Adjust cohort filters and calculation parameters there.

Validate the DAG without running jobs:

```bash
snakemake --dry-run --software-deployment-method conda --cores 1
```

Run unit tests with:

```bash
python -m pip install -e '.[test]'
pytest
```
