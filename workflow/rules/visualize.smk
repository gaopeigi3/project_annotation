rule visualize:
    input:
        h5ad=f"{config['paths']['results_root']}/{config['cohort']['name']}/annotated.h5ad"

    output:
        umap_celltype=f"{config['paths']['results_root']}/{config['cohort']['name']}/plots/umap_celltype.png",
        umap_sample=f"{config['paths']['results_root']}/{config['cohort']['name']}/plots/umap_sample.png"

    log:
        f"{config['paths']['logs_root']}/{config['cohort']['name']}/visualize.log"

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