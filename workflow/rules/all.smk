COHORT = config["cohort"]["name"]

rule all:
    default_target: True
    input:
        f"{config['paths']['results_root']}/{COHORT}/annotated.h5ad",
        f"{config['paths']['results_root']}/{COHORT}/cluster_scores.csv",
        f"{config['paths']['results_root']}/{COHORT}/plots/umap_celltype.png",
        f"{config['paths']['results_root']}/{COHORT}/plots/umap_sample.png"