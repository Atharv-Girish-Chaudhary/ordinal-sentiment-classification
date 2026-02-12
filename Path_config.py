"""
Shared path configuration for all notebooks.
Import this at the top of each notebook:
    from path_config import DATA_RAW, DATA_PROCESSED, FIGURES, TABLES
"""

from pathlib import Path

# Project root (one level up from notebooks/)
ROOT = Path(__file__).resolve().parent.parent

# Data
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"

# Results
FIGURES = ROOT / "results" / "figures"
TABLES = ROOT / "results" / "tables"

# Docs
DOCS = ROOT / "docs"

# Create directories if they don't exist
for d in [DATA_RAW, DATA_PROCESSED, FIGURES, TABLES, DOCS]:
    d.mkdir(parents=True, exist_ok=True)