rule reduce:
    input:
        h5ad=f"results/{config['cohort']['name']}/integrated.h5ad"

    output:
        h5ad=f"results/{config['cohort']['name']}/clustered.h5ad"

    params:
        n_neighbors=config["params"]["reduce"]["n_neighbors"],
        resolution=config["params"]["reduce"]["resolution"],
        method=config["params"]["integrate"]["method"]

    log:
        f"logs/{config['cohort']['name']}/reduce.log"

    conda:
        "../../envs/scanpy.yaml"

    shell:
        """
        PYTHONPATH=src:. python workflow/scripts/processing/reduce.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --n-neighbors {params.n_neighbors} \
            --resolution {params.resolution} \
            --method {params.method} \
            > {log} 2>&1
        """