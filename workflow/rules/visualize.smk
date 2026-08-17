rule visualize:
    input:
        h5ad=f"results/{config['cohort']['name']}/annotated.h5ad"

    output:
        umap_celltype=f"results/{config['cohort']['name']}/plots/umap_celltype.png",
        umap_sample=f"results/{config['cohort']['name']}/plots/umap_sample.png"

    log:
        f"logs/{config['cohort']['name']}/visualize.log"

    conda:
        "../../envs/scanpy.yaml"

    shell:
        """
        PYTHONPATH=src:. python workflow/scripts/analysis/visualize.py \
            --input {input.h5ad} \
            --umap-celltype {output.umap_celltype} \
            --umap-sample {output.umap_sample} \
            > {log} 2>&1
        """