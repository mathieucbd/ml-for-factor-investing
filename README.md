# ML for Factor Investing

Practical implementation in Python of the book *Machine Learning for Factor Investing*, written by Guillaume Coqueret and Tony Guida.

## Project Structure

```
ml-for-factor-investing/
├── data/                          # Data directory (files not tracked)
│   ├── raw/                       # Raw data files
│   ├── processed/                 # Processed and cleaned data
│   └── output/                    # Model outputs and results
├── notebooks/
│   ├── 01_data.ipynb             # Data exploration and loading
│   ├── 02_factors.ipynb          # Factor analysis and Fama-MacBeth regressions
│   ├── 3_data_preprocessing.ipynb # Data cleaning and feature engineering
│   ├── 4_penalized_regressions.ipynb # Lasso and Ridge regression models
│   ├── 5_tree_based_methods.ipynb    # Decision trees and random forests
│   ├── 6_neural_networks.ipynb       # Deep learning models
│   ├── 7_support_vector_machines.ipynb # SVM models
│   ├── 8_bayesian_methods.ipynb      # Bayesian inference approaches
│   ├── 9_validating_and_tuning.ipynb # Model validation and hyperparameter tuning
│   ├── 10_ensemble_models.ipynb      # Ensemble methods and stacking
│   ├── 11_portfolio_backtesting.ipynb # Portfolio construction and backtesting
│   └── 12_interpretability.ipynb     # Model interpretability (LIME, SHAP, DALEX)
├── models/                        # Model storage directory
├── utils.py                       # Utility functions
├── .env                           # Environment variables (not tracked)
├── .gitignore
├── pyproject.toml                 # Project dependencies and metadata
├── uv.lock                        # UV package manager lock file
└── README.md
```

## Setup

### Prerequisites

- Python 3.10+
- Virtual environment (recommended)
- [uv](https://github.com/astral-sh/uv) package manager (optional, for faster installation)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mathieucbd/ml-for-factor-investing.git
cd ml-for-factor-investing
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate    # Linux/Mac
```

3. Install dependencies:
```bash
# Using pip
pip install -e .

# Or using uv for faster installation (recommended)
uv pip install -e .
```

This will install all required packages including:
- Data science: pandas, numpy, matplotlib, seaborn
- Machine learning: scikit-learn, xgboost, tensorflow, keras
- Bayesian methods: pymc, numpyro, arviz, bartz
- Interpretability: lime, shap, dalex
- Optimization: scikit-optimize, cvxopt
- Data access: fredapi
- And more (see pyproject.toml for full list)

### Data

The project requires data files in the `data/raw/` directory:

1. **data_ml.csv** - Stock returns and characteristics data (~134MB)
   - Too large for git, obtain from the book's companion website or data source
2. **F-F_Research_Data_5_Factors_2x3.csv** - Fama-French 5-factor data
   - Download from: [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

These files are not tracked in git due to size constraints. Place them in `data/raw/` after cloning.

Additional directories:
- `data/processed/` - For cleaned and preprocessed data (e.g., macro_cond.csv)
- `data/output/` - For model outputs and results

## Usage

### Running the Notebooks

The notebooks are designed to be run in VS Code with Jupyter extension or in Jupyter Lab:

```bash
# If using standalone Jupyter
jupyter lab
```

**Notebooks in order:**
1. `01_data.ipynb` - Data exploration and loading
2. `02_factors.ipynb` - Factor analysis and Fama-MacBeth regressions
3. `03_data_preprocessing.ipynb` - Data cleaning and feature engineering
4. `04_penalized_regressions.ipynb` - Lasso, Ridge, and Elastic Net regression models
5. `05_tree_based_methods.ipynb` - Decision trees, random forests, and XGBoost
6. `06_neural_networks.ipynb` - Deep learning models with TensorFlow/Keras
7. `07_support_vector_machines.ipynb` - Support vector machine implementations
8. `08_bayesian_methods.ipynb` - Bayesian inference and probabilistic methods
9. `09_validating_and_tuning.ipynb` - Model evaluation, validation, and hyperparameter tuning
10. `10_ensemble_models.ipynb` - Ensemble methods and model stacking
11. `11_portfolio_backtesting.ipynb` - Portfolio construction and backtesting strategies
12. `12_interpretability.ipynb` - Model interpretability with LIME, SHAP, and DALEX

## Notes

- Data files in `data/raw/` are excluded from version control due to size (data_ml.csv is 133.74 MB, exceeding GitHub's 100 MB limit)
- Fama-French factor data uses month-start dates (YYYYMM01) while stock data uses month-end dates
- The notebooks use year-month period matching to align these different date conventions
- Environment variables (e.g., FRED API key) should be stored in `.env` file (not tracked)
- The project uses `pyproject.toml` for dependency management with modern Python packaging standards
- `uv.lock` ensures reproducible builds when using the uv package manager

## Key Libraries

- **scikit-learn**: Traditional ML algorithms (regression, trees, SVM)
- **XGBoost**: Gradient boosting implementation
- **TensorFlow/Keras**: Deep learning frameworks
- **PyMC & NumPyro**: Bayesian inference
- **LIME, SHAP, DALEX**: Model interpretability and explainability
- **statsmodels**: Statistical modeling and econometrics

## License

This project is for educational and research purposes.
MIT License

## Author

Mathieu Chabirand
