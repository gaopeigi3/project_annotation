lymphoid_schema = {

    # =========================================================
    # CD4 T
    # =========================================================
    "CD4": {
        "color": "#8dd3c7",
        "markers": {
            "general": ["CD4", "IL7R", "MAL", "LTB"]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {
                    "CD4 Memory T cells": {
                        "color": "#66c2a5",
                        "markers": ["CXCR3", "IL7R", "LTB"]
                    },
                    "CD4 Naive T cells": {
                        "color": "#99d8c9",
                        "markers": ["LEF1", "TCF7", "SELL", "CD44"]
                    },
                    "CD4 CTL T cells": {
                        "color": "#41ae76",
                        "markers": ["GZMB", "PRF1", "GNLY", "NKG7"]
                    },
                    "CD4 Exhausted T cells": {
                        "color": "#238b45",
                        "markers": ["CTLA4", "LAG3", "TIGIT", "HAVCR2", "PDCD1"]
                    },
                    "CD4 Th1 T cells": {
                        "color": "#005824",
                        "markers": ["TBX21", "STAT4", "IFNG", "IL12A"]
                    },
                    "CD4 Th2 T cells": {
                        "color": "#b2e2e2",
                        "markers": ["STAT6", "GATA6", "IL4"]
                    },
                    "CD4 Th17 T cells": {
                        "color": "#7bccc4",
                        "markers": ["IL7RA", "STAT3", "RORC"]
                    },
                    "CD4 Tfh T cells": {
                        "color": "#2ca25f",
                        "markers": ["BCL6", "CXCR5"]
                    },
                    "Treg": {
                        "color": "#006d2c",
                        "markers": ["TGFB1", "FOXP3", "IL2RA", "IKZF2"]
                    }
                }
            }
        }
    },

    # =========================================================
    # CD8 T
    # =========================================================
    "CD8": {
        "color": "#fb8072",
        "markers": {
            "general": ["CD8A", "CD8B", "CD3D"]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {
                    "CD8 Naive T cells": {
                        "color": "#fdbb84",
                        "markers": ["NELL2", "CD8B", "CCR7", "LEF1", "SELL", "IL7R"]
                    },
                    "CD8 Effector Memory T cells": {
                        "color": "#e34a33",
                        "markers": ["PRF1", "FGFBP2", "FCGR3A", "KLRD1", "NKG7", "KLRG1", "CX3CR1"]
                    },
                    "CD8 Exhausted T cells": {
                        "color": "#b30000",
                        "markers": ["CTLA4", "LAG3", "TIGIT", "PDCD1", "TOX"]
                    },
                    "CD8 CTL T cells": {
                        "color": "#f16913",
                        "markers": ["GZMB", "PRF1", "GNLY", "NKG7", "GZMA"]
                    },
                    "MAIT": {
                        "color": "#fb6a4a",
                        "markers": ["KLRB1", "IL7R", "SLC4A10", "RORC"]
                    }
                }
            }
        }
    },

    # =========================================================
    # B cells
    # =========================================================
    "B": {
        "color": "#80b1d3",
        "markers": {
            "general": ["MS4A1", "CD79A", "CD79B", "BANK1", "RALGPS2"]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {
                    "B intermediate": {
                        "color": "#4eb3d3",
                        "markers": [
                            "MS4A1", "TNFRSF13B", "IGHM", "IGHD",
                            "AIM2", "CD79A", "LINC01857",
                            "RALGPS2", "BANK1", "CD79B"
                        ]
                    },
                    "B memory": {
                        "color": "#2b8cbe",
                        "markers": [
                            "MS4A1", "COCH", "AIM2", "BANK1",
                            "SSPN", "CD79A", "TEX9",
                            "RALGPS2", "TNFRSF13C", "LINC01781"
                        ]
                    },
                    "B naive": {
                        "color": "#7fcdbb",
                        "markers": [
                            "IGHM", "IGHD", "CD79A", "IL4R",
                            "MS4A1", "CXCR4", "BTG1",
                            "TCL1A", "CD79B", "YBX3"
                        ]
                    },
                    "Plasmablast": {
                        "color": "#1c9099",
                        "markers": [
                            "IGHA2", "MZB1", "TNFRSF17", "DERL3",
                            "TXNDC5", "TNFRSF13B", "POU2AF1",
                            "CPNE5", "HRASLS2", "NT5DC2"
                        ]
                    }
                }
            }
        }
    },

    # =========================================================
    # pre B
    # =========================================================
    "pre B": {
        "color": "#08306b",
        "markers": {
            "general": [
                "NPY", "LCN6", "RAG2", "HMHB1",
                "ARPP21", "AKAP12", "RAG1",
                "C10orf10", "CYGB", "SLC8A1-AS1"
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
    # NK
    # =========================================================
    "NK": {
        "color": "#fccde5",
        "markers": {
            "general": ["TRDC", "FCER1G", "KLRF1"]
        },
        "modules": {
            "basic": {
                "enabled_by_default": True,
                "resolution": "broad",
                "description": "...",
                "subtypes": {
                "NK CD56-dim": {
                    "color": "#fa9fb5",
                    "markers": [
                        "GNLY", "TYROBP", "NKG7",
                        "GZMB", "PRF1", "FGFBP2", "SPON2"
                    ]
                },
                "NK Proliferating": {
                    "color": "#dd3497",
                    "markers": [
                        "MKI67", "TYMS", "TOP2A",
                        "PCLAF", "CD247", "CLSPN", "ASPM"
                    ]
                },
                "NK CD56-bright": {
                    "color": "#980043",
                    "markers": [
                        "XCL2", "SPINK2", "KLRC1",
                        "XCL1", "SPTSSB", "PPP1R9A",
                        "NCAM1", "TNFRSF11A"
                        ]
                    }
                }
            }
        }
    },

}