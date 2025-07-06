# Data Exploration

This folder contains the Jupyter notebook used to **explore and understand**
our cleaned Student Engagement Dataset (SED).

## Dataset

- **File used:** [`cleaned_sed_dataset.csv`](2_data_preparation\cleaned_data\cleaned_sed_dataset.csv)
- Contains aggregated student engagement features (e.g., number of forum posts,
assignments, logins) along with average marks.

## Notebook Contents

- Loads and inspects the cleaned dataset
- Checks for missing values
- Generates descriptive statistics
- Visualizes data with:
  - Histograms
  - Boxplots
  - Correlation heatmaps
  - Scatter plots comparing engagement metrics to performance

## Purpose

- Helps understand data structure
- Reveals potential relationships between features and target
- Informs later modeling without modifying the data

## How to Run

Open the notebook in Jupyter or Google Colab and run all cells.
Ensure `cleaned_sed_dataset.csv` is present in the expected path.
