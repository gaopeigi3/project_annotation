myeloid_schema = {
    # =========================================================
    # Monocytes
    # =========================================================
    "Mono": {
        "color": "#bebada",
        "markers": {
            "general": [
                "LYPD2", "FOLR3", "CLEC4E", "LILRA1",
                "CDA", "RBP7", "CD300LF",
                "FPR1", "CD93", "MTMR11"
            ]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {
                    "CD14 Mono": {
                        "color": "#9e9ac8",
                        "markers": [
                            "FOLR3", "CLEC4E", "MCEMP1", "RBP7",
                            "CDA", "FPR1", "CD300E",
                            "C5AR1", "CD93", "APOBEC3A"
                        ]
                    },
                    "CD16 Mono": {
                        "color": "#756bb1",
                        "markers": [
                            "LYPD2", "VMO1", "TPPP3", "C1QA",
                            "C5AR1", "CD300E", "GPBAR1",
                            "LILRA1", "HES4", "APOBEC3A"
                        ]
                    }
                }
            }
        }
    },
        
    # =========================================================
    # Macrophage
    # =========================================================
    "Macrophage": {
        "color": "#ffed6f",

        "markers": {
            "general": [
                "SPIC", "FABP3", "CD5L", "CCL18",
                "C1QC", "C1QB", "FABP4",
                "C1QA", "APOE", "SELENOP"
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
    # DC
    # =========================================================
    "DC": {
        "color": "#b3de69",
        "markers": {
            "general": [
                "CLEC4C", "PROC", "SCT", "SCN9A",
                "SHD", "PPM1J", "ENHO",
                "CLEC10A", "LILRA4", "DNASE1L3"
            ]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {
                    "ASDC": {
                        "color": "#66c2a5",
                        "markers": [
                            "PPP1R14A", "LILRA4", "AXL",
                            "IL3RA", "SCT", "SCN9A",
                            "LGMN", "DNASE1L3",
                            "CLEC4C", "GAS6"
                        ]
                    },
                    "cDC1": {
                        "color": "#31a354",
                        "markers": [
                            "CLEC9A", "DNASE1L3", "C1orf54",
                            "IDO1", "CLNK", "CADM1",
                            "FLT3", "ENPP1", "XCR1", "NDRG2"
                        ]
                    },
                    "cDC2": {
                        "color": "#006d2c",
                        "markers": [
                            "FCER1A", "HLA-DQA1", "CLEC10A",
                            "CD1C", "ENHO", "PLD4",
                            "GSN", "SLC38A1", "NDRG2", "AFF3"
                        ]
                    },
                    "pDC": {
                        "color": "#b2df8a",
                        "markers": [
                            "ITM2C", "PLD4", "SERPINF1",
                            "LILRA4", "IL3RA", "TPM2",
                            "MZB1", "SPIB", "IRF4", "SMPD3"
                        ]
                    }
                }
            }
        }
    },

}