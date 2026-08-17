rule integrate:
    input:
        h5ad=f"results/{config['cohort']['name']}/preprocessed.h5ad"

    output:
        h5ad=f"results/{config['cohort']['name']}/integrated.h5ad"

    params:
        method=config["params"]["integrate"]["method"],
        key=config["params"]["integrate"]["key"]

    log:
        f"logs/{config['cohort']['name']}/integrate.log"

    conda:
        "envs/scanpy.yaml"

    shell:
        """
        python workflow/scripts/processing/integrate.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --method {params.method} \
            --key {params.key} \
            > {log} 2>&1
        """