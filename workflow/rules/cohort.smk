rule cohort:
    input:
        h5ad=config["data"]["input_h5ad"]
    output:
        h5ad=f"results/{config['cohort']['name']}/cohort.h5ad"
    params:
        filters=lambda wildcards: json.dumps(config["cohort"]["filters"])
    log:
        f"logs/{config['cohort']['name']}/cohort.log"
    conda:
        "envs/scanpy.yaml"
    shell:
        """
        python workflow/scripts/processing/select_cohort.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --filters '{params.filters}' \
            > {log} 2>&1
        """