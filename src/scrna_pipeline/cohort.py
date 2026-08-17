import numpy as np


def select_cohort(adata, filters):
    mask = np.ones(adata.n_obs, dtype=bool)

    for column, allowed_values in filters.items():
        if column not in adata.obs.columns:
            raise KeyError(
                f"Column '{column}' not found in adata.obs"
            )
        mask &= adata.obs[column].isin(allowed_values)

    selected = adata[mask].copy()
    if selected.n_obs == 0:
        raise ValueError("Cohort selection returned 0 cells.")
    return selected