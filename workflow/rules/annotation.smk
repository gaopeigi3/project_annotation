rule annotation:
    input:
        h5ad=f"results/{config['cohort']['name']}/clustered.h5ad"

    output:
        h5ad=f"results/{config['cohort']['name']}/annotated.h5ad",
        scores=f"results/{config['cohort']['name']}/cluster_scores.csv"

    params:
        threshold_main=config["params"]["annotation"]["threshold_main"],
        threshold_sub=config["params"]["annotation"]["threshold_sub"]

    log:
        f"logs/{config['cohort']['name']}/annotation.log"

    conda:
        "envs/scanpy.yaml"

    shell:
        """
        python workflow/scripts/analysis/annotation.py \
            --input {input.h5ad} \
            --output {output.h5ad} \
            --scores {output.scores} \
            --threshold-main {params.threshold_main} \
            --threshold-sub {params.threshold_sub} \
            > {log} 2>&1
        """