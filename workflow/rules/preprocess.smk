rule preprocess:
    input:
        h5ad=f"{config['paths']['results_root']}/{config['cohort']['name']}/qc.h5ad"
    output:
        h5ad=f"{config['paths']['results_root']}/{config['cohort']['name']}/preprocessed.h5ad"
    log:
        f"{config['paths']['logs_root']}/{config['cohort']['name']}/preprocess.log"
    conda:
        "../../envs/scanpy.yaml"
    params:
        n_hvg=config["params"]["preprocess"]["n_hvg"],
        min_cells=config["params"]["preprocess"]["min_cells"],
        remove_mt="--remove-mt" if config["params"]["preprocess"]["remove_mt"] else "--no-remove-mt",
        remove_ribo="--remove-ribo" if config["params"]["preprocess"]["remove_ribo"] else "--no-remove-ribo"
    shell:
        """
        PYTHONPATH=src:. python workflow/scripts/processing/preprocess.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --n-hvg {params.n_hvg} \
            --min-cells {params.min_cells} \
            {params.remove_mt} \
            {params.remove_ribo} \
            > {log} 2>&1
        """