progenitor_schema = {
    # =========================================================
    # HSC
    # =========================================================
    "HSC": {
        "color": "#bc80bd",
        "markers": {
            "general": ["CD34", "AVP", "CRHBP"]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {}
            },
            "developmental": {
                "enabled_by_default": False,
                "resolution": "developmental",
                "description": "...",
                "subtypes": {
                    "MonocyticLineage": {
                    "color": "#9e5fa8",
                    "markers": ["LYZ", "S100A8", "S100A9", "ITGAM"]
                },
                "Antigen": {
                    "color": "#d9a8db",
                    "markers": ["CD74", "HLA-DRA", "HLA-DRB1", "CIITA"]
                }
                    }
                }
        }
    },

    # =========================================================
    # CLP
    # =========================================================
    "CLP": {
        "color": "#8c6bb1",

        "markers": {
            "general": [
                "ACY3", "PRSS2", "C1QTNF4", "SPINK2",
                "SMIM24", "NREP", "CD34",
                "DNTT", "FLT3", "SPNS3"
            ]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {}
            }
        }
    },

    # =========================================================
    # GMP
    # =========================================================
    "GMP": {
        "color": "#88419d",

        "markers": {
            "general": [
                "SERPINB10", "RNASE3", "MS4A3",
                "PRTN3", "ELANE", "AZU1",
                "CTSG", "RNASE2", "RETN", "NPW"
            ]
        },
    "modules": {
        "basic": {
            "enabled_by_default": True,
            "resolution": "broad",
            "description": "...",
            "subtypes": {}
        }
    }
    },

    # =========================================================
    # Unknown
    # =========================================================
    "Unknown": {
        "color": "#999999",

        "markers": {
            "general": []
        },
    "modules": {
        "basic": {
            "enabled_by_default": True,
            "resolution": "broad",
            "description": "...",
            "subtypes": {}
        }
    }
    },
}