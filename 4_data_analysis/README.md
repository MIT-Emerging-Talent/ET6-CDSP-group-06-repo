# Data Analysis

This folder contains the Jupyter notebook used to **model and analyze**
student performance data.

## Dataset

- **File used:** [`cleaned_sed_dataset.csv`](2_data_preparation\cleaned_data\cleaned_sed_dataset.csv)
- Same cleaned dataset from the data preparation stage.

## Notebook Contents

- Loads the prepared dataset
- Selects relevant features for modeling
- Splits data into training and testing sets
- Trains a linear regression model
- Evaluates predictions using Mean Squared Error (≈107) and R² score (≈0.69)
- Visualizes actual vs. predicted average marks
- Extracts and plots feature coefficients to interpret importance

## Purpose

This analysis moves beyond EDA to:

- Build a simple, interpretable baseline model
- Identify which engagement features most influence student marks
- Evaluate predictive power and understand limitations

## How to Run

Open the notebook in Jupyter or Google Colab and run all cells. Ensure
`cleaned_sed_dataset.csv` is present in the expected path.
