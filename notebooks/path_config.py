"""
Path configuration for notebooks.
Add this cell at the beginning of notebooks to set up paths correctly.

Usage in notebook:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath('')))
    from path_config import DATA_DIR, RESULTS_DIR, FIGURES_DIR, TABLES_DIR
"""

import os

# Get the project root directory (parent of notebooks/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define directory paths
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
DATA_RAW_DIR = os.path.join(DATA_DIR, 'raw')
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
RESULTS_DIR = os.path.join(PROJECT_ROOT, 'results')
FIGURES_DIR = os.path.join(RESULTS_DIR, 'figures')
TABLES_DIR = os.path.join(RESULTS_DIR, 'tables')

# Common file paths
CLEANED_DATA_FILE = os.path.join(DATA_PROCESSED_DIR, 'amazon_electronics_cleaned.csv')
NOMINAL_RESULTS_FILE = os.path.join(TABLES_DIR, 'nominal_results.csv')
ORDINAL_RESULTS_FILE = os.path.join(TABLES_DIR, 'ordinal_results.csv')
FINAL_RESULTS_FILE = os.path.join(TABLES_DIR, 'final_results_table.csv')

# Create directories if they don't exist
for directory in [DATA_RAW_DIR, DATA_PROCESSED_DIR, FIGURES_DIR, TABLES_DIR]:
    os.makedirs(directory, exist_ok=True)

