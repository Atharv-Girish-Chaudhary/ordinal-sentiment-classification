# Ordinal Sentiment Classification

A machine learning project comparing nominal and ordinal encoding approaches for sentiment classification on Amazon electronics reviews.

## Project Overview

This project explores the effectiveness of treating sentiment classification as an ordinal problem versus a nominal classification problem. The study uses Amazon electronics review data and compares various machine learning models under both encoding schemes.

## Project Structure

```
ordinal-sentiment-classification/
├── data/                          # Dataset files
│   ├── electronics.json.gz       # Raw Amazon electronics reviews dataset
│   └── amazon_electronics_cleaned.csv  # Processed and cleaned dataset
│
├── docs/                          # Documentation and reports
│   ├── IEEE_Report_Full.pdf      # Full IEEE format research report
│   ├── Final_Project_Presentation.pptx  # Project presentation slides
│   └── *.pdf                     # Additional reference documents
│
├── notebooks/                     # Jupyter notebooks for analysis
│   ├── 1_Data_Loading.ipynb      # Data loading and preprocessing
│   ├── 2_EDA_Visualization.ipynb # Exploratory data analysis and visualizations
│   ├── 3_Models_Nominal.ipynb    # Nominal classification models
│   ├── 4_Models_Ordinal.ipynb    # Ordinal classification models
│   ├── 5_Results_Analysis.ipynb  # Comprehensive results analysis
│   └── 6_Additional_Visualizations.ipynb  # Additional visualizations
│
└── results/                       # Generated results and outputs
    ├── figures/                  # Visualization figures
    │   ├── confusion_matrices_*.png
    │   ├── model_comparison*.png
    │   ├── ordinal_vs_nominal.png
    │   └── fig_*.png             # Publication-ready figures
    └── tables/                   # Results tables
        ├── final_results_table.csv
        ├── nominal_results.csv
        ├── ordinal_results.csv
        └── *_predictions.csv
```

## Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook
- Required Python packages (install via `pip install -r requirements.txt` if available)

### Usage

1. **Data Loading**: Start with `1_Data_Loading.ipynb` to load and preprocess the dataset
2. **Exploratory Analysis**: Run `2_EDA_Visualization.ipynb` to explore the data
3. **Model Training**: 
   - Run `3_Models_Nominal.ipynb` for nominal classification models
   - Run `4_Models_Ordinal.ipynb` for ordinal classification models
4. **Results Analysis**: Execute `5_Results_Analysis.ipynb` for comprehensive results comparison
5. **Additional Visualizations**: Use `6_Additional_Visualizations.ipynb` for extra figures

## Key Findings

Results comparing nominal vs ordinal approaches are available in:
- `results/tables/final_results_table.csv` - Summary of all model performances
- `results/figures/` - Visual comparisons and analysis plots

## Documentation

- Full research report: `docs/IEEE_Report_Full.pdf`
- Project presentation: `docs/Final_Project_Presentation.pptx`

## License

See [LICENSE](LICENSE) file for details.
