# Ordinal vs Nominal Sentiment Analysis

**CS 5100 Final Project - Northeastern University**

This project compares ordinal and nominal classification approaches for 5-star rating prediction on Amazon Electronics Reviews. We investigate whether treating ratings as ordered (ordinal) rather than unordered (nominal) categories improves model performance, particularly in reducing severe misclassifications.

## Dataset Overview

- **Dataset**: Amazon Reviews 2023
- **Category**: Electronics
- **Source**: McAuley Lab, UCSD
- **Size**: 18.3M users, 1.6M items, 43.9M reviews
- **Time Range**: May 1996 - September 2023

## Quick Start

### Prerequisites

Make sure you have the following Python packages installed:

```bash
pip install pandas numpy matplotlib seaborn plotly datasets jupyter
```

### Running the Analysis

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run notebooks in sequence**:
   ```bash
   jupyter notebook notebooks/
   ```
   
   Execute notebooks in order:
   - `1_Data_Loading.ipynb` - Load and clean data
   - `2_EDA_Visualization.ipynb` - Exploratory data analysis
   - `3_Models_Nominal.ipynb` - Train nominal models
   - `4_Models_Ordinal.ipynb` - Train ordinal models
   - `5_Results_Analysis.ipynb` - Compare and analyze results
   - `6_Additional_Visualizations.ipynb` - Generate publication figures

## Research Question

**Do the performance gains from ordinal treatment of 5-star ratings justify the increased model complexity?**

## Models Compared

### Nominal Models (Unordered Categories)
1. **Multinomial Naive Bayes** - Baseline nominal classifier
2. **Logistic Regression (Multinomial)** - Softmax-based classification

### Ordinal Models (Ordered Categories)
1. **Ridge Regression** - Treats ratings as continuous, rounds to nearest integer
2. **Ordinal Logistic Regression** - Threshold-based approach using cumulative probabilities

## Key Results

- **Best Accuracy**: Logistic Regression (Nominal) - 65.95%
- **Lowest MAE**: Logistic Regression (Nominal) - 0.5337
- **Lowest Severe Error**: Ridge Regression (Ordinal) - 18.1%
- **Key Finding**: Ordinal models reduce severe misclassifications (18-35% vs 35-44% for nominal)

## Key Findings

1. **Ordinal models reduce severe errors**: Ridge Regression achieves 18.1% severe error rate vs 35-44% for nominal models
2. **Adjacent rating confusion**: 55-82% of errors occur between adjacent ratings (e.g., 4↔5 stars)
3. **Class imbalance challenge**: 5-star reviews dominate (~60%), affecting minority class performance
4. **MAE improvement**: Ordinal methods show better mean absolute error, indicating better ordinal structure understanding

## Project Structure

```
├── README.md                         # Project documentation
├── requirements.txt                  # Python dependencies
├── Final_Project_Presentation.pptx   # Presentation slides
│
├── notebooks/                        # Jupyter notebooks
│   ├── 1_Data_Loading.ipynb          # Data loading and preprocessing
│   ├── 2_EDA_Visualization.ipynb     # Exploratory data analysis
│   ├── 3_Models_Nominal.ipynb        # Nominal classification models
│   ├── 4_Models_Ordinal.ipynb        # Ordinal classification models
│   ├── 5_Results_Analysis.ipynb      # Results comparison and analysis
│   ├── 6_Additional_Visualizations.ipynb  # Publication-quality figures
│   ├── path_config.py                # Path configuration helper
│   └── archive/                      # Archived/experimental notebooks
│
├── data/
│   ├── raw/                          # Raw dataset files (.json.gz, .jsonl.gz)
│   └── processed/                    # Cleaned data (amazon_electronics_cleaned.csv)
│
├── results/
│   ├── figures/                      # All visualization images
│   └── tables/                       # Result CSV files
│
└── docs/                             # Project documents, reports, and PDFs
    ├── IEEE_Report_Full.pdf          # Final IEEE-format report
    └── Video_Script.md               # Presentation video script
```

## Technical Details

### Data Sources
- **Reviews Data**: User reviews with ratings, text, timestamps, and metadata
- **Product Metadata**: Product information including prices, categories, and descriptions

### Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib/seaborn**: Static visualizations
- **plotly**: Interactive visualizations
- **datasets**: Hugging Face dataset loading

### Data Processing
- Timestamp conversion to datetime objects
- Feature engineering for temporal analysis
- Data cleaning and preprocessing
- Statistical analysis and correlation studies

## Future Enhancements

1. **Sentiment Analysis**: Analyze review text for deeper insights
2. **Product Clustering**: Group similar products based on review patterns
3. **Predictive Modeling**: Predict product success from early reviews
4. **Competitive Analysis**: Compare electronics subcategories
5. **User Segmentation**: Identify user personas based on behavior

## References

- [Amazon Reviews 2023 Dataset](https://amazon-reviews-2023.github.io/)
- [McAuley Lab, UCSD](https://cseweb.ucsd.edu/~jmcauley/)
- [Hugging Face Datasets](https://huggingface.co/datasets)

## Citation

If you use this analysis or the dataset, please cite:

```bibtex
@article{hou2024bridging,
  title={Bridging Language and Items for Retrieval and Recommendation},
  author={Hou, Yupeng and Li, Jiacheng and He, Zhankui and Yan, An and Chen, Xiusi and McAuley, Julian},
  journal={arXiv preprint arXiv:2403.03952},
  year={2024}
}
```

## Contributing

Feel free to contribute to this project by:
- Adding new visualizations
- Improving existing analysis
- Adding support for other product categories
- Enhancing documentation

## License

This project is for educational and research purposes. Please refer to the original dataset license for usage terms.

## Contact

For questions or suggestions about this analysis, please open an issue in this repository.

---

**Note**: This analysis is part of a CS 5100 Final Project at Northeastern University.
