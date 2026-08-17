rule annotation:
    input:
        h5ad=f"{config['paths']['results_root']}/{config['cohort']['name']}/clustered.h5ad"

    output:
        h5ad=f"{config['paths']['results_root']}/{config['cohort']['name']}/annotated.h5ad",
        scores=f"{config['paths']['results_root']}/{config['cohort']['name']}/cluster_scores.csv"

    params:
        threshold_main=config["params"]["annotation"]["threshold_main"],
        threshold_sub=config["params"]["annotation"]["threshold_sub"],
        version=config["params"]["annotation"]["version"]

    log:
        f"{config['paths']['logs_root']}/{config['cohort']['name']}/annotation.log"

    conda:
        "../../envs/scanpy.yaml"

    shell:
        """
        PYTHONPATH=src:. python workflow/scripts/analysis/annotation.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --scores {output.scores} \
            --threshold-main {params.threshold_main} \
            --threshold-sub {params.threshold_sub} \
            --version {params.version} \
            > {log} 2>&1
        """
