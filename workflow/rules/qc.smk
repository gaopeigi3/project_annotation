rule qc:
    input:
        h5ad=f"results/{config['cohort']['name']}/cohort.h5ad"
    output:
        h5ad=f"results/{config['cohort']['name']}/qc.h5ad"
    params:
        min_genes=config["params"]["qc"]["min_genes"],
        max_mt=config["params"]["qc"]["max_mt"]
    log:
        "logs/qc.log"
    conda:
        "envs/scanpy.yaml"
    shell:
        """
        python workflow/scripts/processing/qc.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --min-genes {params.min_genes} \
            --max-mt {params.max_mt} \
            > {log} 2>&1
        """