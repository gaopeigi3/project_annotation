import json

configfile: "config/config.yaml"

include: "workflow/rules/all.smk"
include: "workflow/rules/cohort.smk"
include: "workflow/rules/qc.smk"
include: "workflow/rules/preprocess.smk"
include: "workflow/rules/integrate.smk"
include: "workflow/rules/reduce.smk"
include: "workflow/rules/annotation.smk"
include: "workflow/rules/visualize.smk"