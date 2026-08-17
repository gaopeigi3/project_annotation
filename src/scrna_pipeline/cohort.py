import numpy as np


def select_cohort(adata, filters):
    mask = np.ones(adata.n_obs, dtype=bool)

    for column, allowed_values in filters.items():
        if column not in adata.obs.columns:
            raise KeyError(
                f"Column '{column}' not found in adata.obs"
            )
        if adata.n_obs == 0:
            raise ValueError("Cohort selection returned 0 cells.")

        mask &= adata.obs[column].isin(allowed_values)

    return adata[mask].copy()