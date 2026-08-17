rule preprocess:
    input:
        h5ad=f"results/{config['cohort']['name']}/qc.h5ad"
    output:
        h5ad=f"results/{config['cohort']['name']}/preprocessed.h5ad"
    log:
        "logs/preprocess.log"
    conda:
        "envs/scanpy.yaml"
    params:
        n_hvg=config["params"]["preprocess"]["n_hvg"]
    shell:
        """
        python workflow/scripts/processing/preprocess.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --n-hvg {params.n_hvg} \
            > {log} 2>&1
        """