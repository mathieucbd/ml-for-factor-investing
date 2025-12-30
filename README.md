# ML for Factor Investing

Practical implementation in Python of the book *Machine Learning for Factor Investing*, written by Guillaume Coqueret and Tony Guida.

## Project Structure

```
ml-for-factor-investing/
├── data/                          # Data directory (files not tracked)
│   ├── raw/
│   ├── processed/
│   └── output/
├── notebooks/
│   ├── 1_data.ipynb              # Data exploration
│   ├── 2_factors.ipynb           # Factor analysis and regressions
│   ├── 3_data_preprocessing.ipynb # Data cleaning and feature engineering
│   ├── 4_penalized_regressions.ipynb # Lasso and Ridge regression models
│   ├── 5_tree_based_methods.ipynb    # Decision trees and random forests
│   ├── 6_neural_networks.ipynb       # Deep learning models
│   ├── 7_support_vector_machines.ipynb # SVM models
│   ├── 8_bayesian_methods.ipynb      # Bayesian inference approaches
│   └── 9_validating_and_tuning.ipynb # Model validation and hyperparameter tuning
├── models/                        # Model storage directory
├── utils.py                       # Utility functions
├── .gitignore
├── pyproject.toml
└── README.md
```

## Setup

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

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
pip install pandas numpy matplotlib scikit-learn xgboost tensorflow statsmodels jupyter scikit-optimize
# or use uv for faster installation:
uv pip install pandas numpy matplotlib scikit-learn xgboost tensorflow statsmodels jupyter scikit-optimize
```

### Data

The project requires two data files in the `data/` directory:

1. **data_ml.csv** - Stock returns and characteristics data (too large for git, ~134MB)
2. **F-F_Research_Data_5_Factors_2x3.csv** - Fama-French 5-factor data
   - Download from: [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

These files are not tracked in git due to size constraints. Place them in the `data/` directory after cloning.

## Usage

### Running the Notebooks

Start Jupyter:
```bash
jupyter notebook
```

Then open notebooks in the `notebooks/` directory in order:
1. `1_data.ipynb` - Data exploration and loading
2. `2_factors.ipynb` - Factor analysis and Fama-MacBeth regressions
3. `3_data_preprocessing.ipynb` - Data cleaning and feature engineering
4. `4_penalized_regressions.ipynb` - Lasso and Ridge regression models
5. `5_tree_based_methods.ipynb` - Decision trees, random forests, and XGBoost
6. `6_neural_networks.ipynb` - Deep learning models with TensorFlow/Keras
7. `7_support_vector_machines.ipynb` - Support vector machine implementations
8. `8_bayesian_methods.ipynb` - Bayesian inference and probabilistic methods
9. `9_validating_and_tuning.ipynb` - Model evaluation, validation, and hyperparameter tuning with GridSearchCV and Bayesian optimization

## Notes

- The `data_ml.csv` file is excluded from version control due to size (133.74 MB exceeds GitHub's 100 MB limit)
- Fama-French factor data uses month-start dates (YYYYMM01) while stock data uses month-end dates
- The notebook uses year-month period matching to align these different date conventions

## License

This project is for educational and research purposes.

## Author

Mathieu Chabirand
