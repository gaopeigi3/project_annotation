erythroid_schema = {
    # =========================================================
    # Erythroid
    # =========================================================

    "Erythroid": {
        "color": "#d9d9d9",
        "markers": {
            "general": [
                "HBD", "HBM", "AHSP", "ALAS2",
                "CA1", "SLC4A1", "IFIT1B",
                "TRIM58", "SELENBP1", "TMCC2"
            ]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {
                    "Early Erythroid": {
                        "color": "#bdbdbd",
                        "markers": [
                        "CNRIP1", "GATA2", "ITGA2B",
                        "TFR2", "GATA1", "KLF1",
                        "CYTL1", "MAP7",
                        "FSCN1", "APOC1"
                    ]
                    },
                    "Late Erythroid": {
                        "color": "#969696",
                        "markers": [
                    "CTSE", "TSPO2", "IFIT1B",
                    "TMEM56", "RHCE", "RHAG",
                    "SPTA1", "ADD2",
                    "EPCAM", "HBG1"
                ]
                    }
                }
            },
            "developmental": {
                "enabled_by_default": False,
                "resolution": "developmental",
                "description": "...",
                "subtypes": {
                    "BFU_E": {...},
                    "CFU_E": {...},
                    "Proerythroblast": {...},
                    "Basophilic_Erythroblast": {...},
                    "Polychromatic_Erythroblast": {...},
                    "Orthochromatic_Erythroblast": {...},
                    "Reticulocyte": {...},
                    "RBC_Mature_Erythrocyte": {...}
                }
            }
        }
    },

    "Platelets": {
        "color": "#a6cee3",
        "markers": {
            "general": [
                "RGS18", "C2orf88", "TMEM40",
                "GP9", "PF4", "PPBP",
                "DAB2", "SPARC",
                "RUFY1", "F13A1"
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
    # EMPs
    # =========================================================
    "EMPs": {
        "color": "#fdb462",
        "markers": {
            "general": [
                "MYCT1", "CRHBP", "NPR3", "AVP",
                "HPGDS", "CRYGD", "IGSF10",
                "PBX1", "CYTL1", "GATA2"
            ]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {},
            },
            "developmental": {
                "enabled_by_default": False,
                "resolution": "developmental",
                "description": "...",
                "subtypes": {
                "Megakaryocyte": {
                    "color": "#f47c3c",
                    "markers": [
                        "GFI1B", "SELP", "GP1BA", "CD9",
                        "ITGA2B", "GATA2", "FLI1",
                        "GP1BB", "VWF", "THPO",
                        "ELF1", "THBS1", "MPIG6B",
                        "GP9", "F2R", "FOG1",
                        "NFE2", "SPI1", "PF4"
                        ]
                    },
                "Erythroid progenitor": {
                    "color": "#fed98e",
                    "markers": [
                        "GATA1", "KLF1", "FCER1A",
                        "ITAG2B", "EPOR", "HBD",
                        "ZFPM1", "GATA2", "GYPA",
                        "TFRC", "TFR2", "CSF2RB",
                        "APOE", "APOC1", "CNRIP1",
                        "FOXO3", "ETS1", "BRD1", "TAL1"
                        ]
                    }
                }
            }
        }    
    },
}