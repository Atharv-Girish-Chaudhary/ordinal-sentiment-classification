# Ordinal vs Nominal Sentiment Classification

**CS 5100 — Foundations of Artificial Intelligence | Northeastern University**

A comparative study of ordinal and nominal encoding approaches for 5-star sentiment classification on Amazon Electronics reviews. We show that ordinal methods — particularly Ridge Regression — reduce severe misclassifications by **48%** compared to nominal classifiers, even when nominal models achieve higher exact-match accuracy.

**Authors:** Atharv Chaudhary, Kien Nguyen, Zijie Liu

---

## Key Results

| Model | Approach | Accuracy | MAE | Severe Error Rate |
|:------|:---------|:--------:|:---:|:-----------------:|
| Multinomial Naive Bayes | Nominal | 63.12% | 0.665 | 44.37% |
| Logistic Regression | Nominal | **65.95%** | **0.534** | 34.83% |
| Ridge Regression | Ordinal | 50.29% | 0.606 | **18.08%** |
| Ordinal Logistic Regression | Ordinal | 65.86% | 0.536 | 34.74% |

**Core finding:** When misclassification cost depends on distance (confusing 1★ with 5★ is worse than 4★ with 5★), ordinal encoding significantly outperforms nominal encoding on the metric that matters most.

---

## Research Question

> Do ordinal approaches to 5-star rating prediction reduce severe misclassifications compared to nominal approaches, and does this justify the trade-off in exact-match accuracy?

---

## Dataset

- **Source:** [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) — McAuley Lab, UCSD
- **Category:** Electronics
- **Samples:** 49,960 reviews after cleaning
- **Class distribution:** Heavily imbalanced (5★: 61.8%, 4★: 17.3%, 3★: 7.2%, 2★: 4.3%, 1★: 5.7%)
- **Features:** TF-IDF vectors (5,000 features, unigrams + bigrams)

---

## Project Structure

```
ordinal-sentiment-classification/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/                              # Run these in order
│   ├── 1_Data_Loading.ipynb                # Load and preprocess reviews
│   ├── 2_EDA_Visualization.ipynb           # Exploratory data analysis
│   ├── 3_Models_Nominal.ipynb              # Naive Bayes + Logistic Regression
│   ├── 4_Models_Ordinal.ipynb              # Ridge Regression + Ordinal Logistic
│   ├── 5_Results_Analysis.ipynb            # Compare all models
│   ├── 6_Additional_Visualizations.ipynb   # Publication-quality figures
│   └── path_config.py                      # Shared path configuration
│
├── data/
│   ├── raw/                                # Original dataset (.json.gz / .jsonl.gz)
│   └── processed/                          # Cleaned CSV after preprocessing
│
├── results/
│   ├── figures/                            # Confusion matrices, comparisons, etc.
│   └── tables/                             # CSV result tables
│
└── docs/
    ├── IEEE_Report_Full.pdf                # Full research report
    ├── Final_Project_Presentation.pptx     # Slide deck
    └── Video_Script.md                     # Presentation script
```

---

## Quick Start

### 1. Clone and install

```bash
git clone https://github.com/Atharv-Girish-Chaudhary/ordinal-sentiment-classification.git
cd ordinal-sentiment-classification
pip install -r requirements.txt
```

### 2. Run notebooks in sequence

```bash
jupyter notebook notebooks/
```

Execute `1_Data_Loading.ipynb` through `6_Additional_Visualizations.ipynb` in order. Each notebook saves its outputs to `data/processed/`, `results/figures/`, or `results/tables/` for downstream notebooks to consume.

### 3. Or download the dataset manually

The data loading notebook fetches from Hugging Face. If that fails, download from [McAuley Lab](https://amazon-reviews-2023.github.io/) and place the `.json.gz` file in `data/raw/`.

---

## Methodology

We compare four models — two nominal, two ordinal — all trained on the same TF-IDF features:

**Nominal (treat ratings as unordered categories):**
- **Multinomial Naive Bayes** — generative baseline using Bayes' theorem with Laplace smoothing
- **Logistic Regression** — discriminative classifier with softmax and cross-entropy loss

**Ordinal (respect the 1 < 2 < 3 < 4 < 5 ordering):**
- **Ridge Regression** — treats ratings as continuous, minimizes squared error (distant errors penalized quadratically), predictions rounded to nearest integer
- **Ordinal Logistic Regression** — learns cumulative probability thresholds via the `mord` library

We introduce a **severe error rate** metric: the percentage of predictions that differ from the true rating by 3+ classes (e.g., predicting 1★ for a 5★ review).

---

## Key Findings

1. **48% reduction in severe errors** — Ridge Regression achieves 18.1% severe error rate vs. ~39.6% average for nominal methods
2. **Accuracy vs. safety trade-off** — Ridge Regression sacrifices exact-match accuracy (50.3% vs. 66.0%) but concentrates errors near the diagonal
3. **Class imbalance hurts everyone** — all models achieve F1 < 0.30 on 2★ and 3★ minority classes
4. **Squared error loss is key** — the quadratic penalty in Ridge (cost of 16 for a 4-class error vs. 1 for a 1-class error) drives the severe error reduction more than ordinal thresholds alone

---

## Future Work

- Address class imbalance via SMOTE, class weighting, or cost-sensitive learning
- Combine deep learning (LSTM, BERT) with ordinal loss functions
- Evaluate generalizability on other domains (hotels, restaurants, movies)
- Hyperparameter tuning to find the accuracy–severity Pareto frontier

---

## Tech Stack

- **Python 3.8+**, NumPy, Pandas, Scikit-learn
- **mord** — ordinal regression models
- **Matplotlib, Seaborn, Plotly** — visualization
- **Hugging Face Datasets** — data loading
- **Jupyter Notebook** — reproducible analysis

---

## Citation

If you use this work or the dataset:

```bibtex
@article{hou2024bridging,
  title={Bridging Language and Items for Retrieval and Recommendation},
  author={Hou, Yupeng and Li, Jiacheng and He, Zhankui and Yan, An and Chen, Xiusi and McAuley, Julian},
  journal={arXiv preprint arXiv:2403.03952},
  year={2024}
}
```

---

## License

This project is for educational and research purposes. See the [original dataset license](https://amazon-reviews-2023.github.io/) for data usage terms.