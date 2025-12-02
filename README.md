# ML for Factor Investing

Practical implementation in Python of the book *Machine Learning for Factor Investing*, written by Guillaume Coqueret and Tony Guida.

## Project Structure

```
ml-for-factor-investing/
├── data/                          # Data directory (files not tracked)
│   └── .gitkeep
├── notebooks/
│   ├── 1_data.ipynb              # Data exploration
│   └── 2_factors.ipynb           # Factor analysis and regressions
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
pip install pandas numpy matplotlib statsmodels jupyter
# or use uv for faster installation:
uv pip install pandas numpy matplotlib statsmodels jupyter
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

Then open notebooks in the `notebooks/` directory:
- `1_data.ipynb` - Explore the dataset
- `2_factors.ipynb` - Factor analysis and Fama-MacBeth regressions

## Notes

- The `data_ml.csv` file is excluded from version control due to size (133.74 MB exceeds GitHub's 100 MB limit)
- Fama-French factor data uses month-start dates (YYYYMM01) while stock data uses month-end dates
- The notebook uses year-month period matching to align these different date conventions

## License

This project is for educational and research purposes.

## Author

Mathieu Chabirand
