rule integrate:
    input:
        h5ad=f"{config['paths']['results_root']}/{config['cohort']['name']}/preprocessed.h5ad"

    output:
        h5ad=f"{config['paths']['results_root']}/{config['cohort']['name']}/integrated.h5ad"

    params:
        method=config["params"]["integrate"]["method"],
        key=config["params"]["integrate"]["key"],
        n_pcs=config["params"]["integrate"]["n_pcs"]

    log:
        f"{config['paths']['logs_root']}/{config['cohort']['name']}/integrate.log"

    conda:
        "../../envs/scanpy.yaml"

    shell:
        """
        PYTHONPATH=src:. python workflow/scripts/processing/integrate.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --method {params.method} \
            --key {params.key} \
            --n-pcs {params.n_pcs} \
            > {log} 2>&1
        """