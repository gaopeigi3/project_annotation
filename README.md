# project_annotation

Author:   
Date: 2026-05-06


# project contract

Input
AnnData (.h5ad)

required obs:
- sample
- batch

optional:
- patient
- condition
Output
obs:
- celltype
- celltype_confidence
- annotation_source
- annotation_version

uns:
- celltype_colors
- annotation_metadata
Guarantee
- reproducible
- deterministic
- resumable
- configurable




## Workflow
raw.h5ad
 ↓
[ preprocess ]
 ↓
[ slicing / cohort selection ]
 ↓
cluster
 ↓
markers
 ↓
annotation
## 


## Run

```bash
snakemake -j 1

---

## 6️⃣ `.gitignore`

```gitignore
data/
results/
logs/
__pycache__/
*.pyc

