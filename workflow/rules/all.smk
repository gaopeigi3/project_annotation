COHORT = config["cohort"]["name"]

rule all:
    input:
        f"results/{COHORT}/annotated.h5ad",
        f"results/{COHORT}/cluster_scores.csv",
        f"results/{COHORT}/plots/umap_celltype.png",
        f"results/{COHORT}/plots/umap_sample.png"