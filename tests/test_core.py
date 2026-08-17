import numpy as np
import pandas as pd
import pytest
from anndata import AnnData

from scrna_pipeline.annotation import annotate_by_marker_voting
from scrna_pipeline.cohort import select_cohort


def test_cohort_rejects_empty_result():
    adata = AnnData(np.ones((2, 2)), obs=pd.DataFrame({"sample": ["a", "b"]}))
    with pytest.raises(ValueError, match="0 cells"):
        select_cohort(adata, {"sample": ["missing"]})


def test_marker_voting_populates_contract_fields():
    adata = AnnData(
        np.array([[1, 1, 0], [1, 1, 0], [0, 0, 1], [0, 0, 1]]),
        obs=pd.DataFrame({"leiden": pd.Categorical(["0", "0", "1", "1"])}),
        var=pd.DataFrame(index=["CD3D", "CD4", "MS4A1"]),
    )
    schema = {
        "T": {"markers": {"general": ["CD3D", "CD4"]}, "modules": {}},
        "B": {"markers": {"general": ["MS4A1"]}, "modules": {}},
    }
    result, mapping, scores = annotate_by_marker_voting(adata, schema, 0.3, 0.4)
    assert mapping == {"0": "T", "1": "B"}
    assert set(result.obs["celltype"]) == {"T", "B"}
    assert (result.obs["celltype_confidence"] == 1.0).all()
    assert not scores.empty
