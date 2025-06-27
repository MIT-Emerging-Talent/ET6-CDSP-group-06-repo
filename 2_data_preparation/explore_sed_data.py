"""
explore_sed_data.py

📊 Initial Data Exploration and
Documentation Script for Milestone 2

This script performs initial
exploratory analysis on the raw
Student Engagement Dataset (SED)
to support Milestone 2 of the
project "Addressing Student
Engagement in Online Learning
Environments".

🔍 Purpose:
- Load raw SED CSV files.
- Inspect their structure using
  `.info()` and `.head()` outputs.
- Generate structured data
  dictionaries for each dataset
  including:
  - Column names
  - Data types
  - Number of unique values
  - Number of missing values
  - (Manual placeholder for column
    descriptions)

📁 Input:
- `1_datasets/raw_data/Student_log/SED_Student_log.csv`
- `1_datasets/raw_data/Student_activity_summary.csv`
- `1_datasets/raw_data/Student_grade_aggregated.csv`
- `1_datasets/raw_data/Student_grade_detailed.csv`

📝 Output:
- Markdown-formatted data
  dictionaries saved to
  `2_data_preparation/cleaned_data/`:
  - `SED_Student_log_data_dictionary.md`
  - `Student_activity_summary_data_dictionary.md`
  - `Student_grade_aggregated_data_dictionary.md`
  - `Student_grade_detailed_data_dictionary.md`

📌 Usage:
This script is intended to help
team members and external
reviewers understand the
structure and quality of the raw
datasets before any cleaning or
feature engineering is performed.

🚫 Warning:
- This script does NOT clean or
  modify the raw data.
- It only generates documentation
  to support transparency and
  reproducibility in the data
  preparation process.
"""

import pandas as pd


def generate_data_dictionary(df):
    """
    Generate a data dictionary from a DataFrame.

    The dictionary includes column names, data types,
    number of unique values, number of missing values,
    and a placeholder for column descriptions.

    Parameters:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        pd.DataFrame: A new DataFrame containing the data dictionary.
    """
    data_dict = []
    for col in df.columns:
        dtype = df[col].dtype
        unique_values = df[col].nunique()
        missing_values = df[col].isnull().sum()
        data_dict.append(
            {
                "Column Name": col,
                "Data Type": str(dtype),
                "Unique Values": unique_values,
                "Missing Values": missing_values,
                "Description": "",  # Placeholder for manual description
            }
        )
    return pd.DataFrame(data_dict)


# Load the datasets
try:
    log_df = pd.read_csv("1_datasets/raw_data/Student_log/SED_Student_log.csv")
    activity_summary_df = pd.read_csv(
        "1_datasets/raw_data/Student_activity_summary.csv"
    )
    grade_aggregated_df = pd.read_csv(
        "1_datasets/raw_data/Student_grade_aggregated.csv"
    )
    grade_detailed_df = pd.read_csv("1_datasets/raw_data/Student_grade_detailed.csv")

    print("--- SED_Student_log.csv Info ---")
    log_df.info()
    print("\n--- SED_Student_log.csv Head ---")
    print(log_df.head())
    log_dict = generate_data_dictionary(log_df)
    log_dict.to_markdown(
        "2_data_preparation/cleaned_data/SED_Student_log_data_dictionary.md",
        index=False,
    )
    print("\nGenerated SED_Student_log_data_dictionary.md")

    print("\n--- Student_activity_summary.csv Info ---")
    activity_summary_df.info()
    print("\n--- Student_activity_summary.csv Head ---")
    print(activity_summary_df.head())
    activity_dict = generate_data_dictionary(activity_summary_df)
    activity_dict.to_markdown(
        "2_data_preparation/cleaned_data/Student_activity_summary_data_dictionary.md",
        index=False,
    )
    print("\nGenerated Student_activity_summary_data_dictionary.md")

    print("\n--- Student_grade_aggregated.csv Info ---")
    grade_aggregated_df.info()
    print("\n--- Student_grade_aggregated.csv Head ---")
    print(grade_aggregated_df.head())
    aggregated_dict = generate_data_dictionary(grade_aggregated_df)
    aggregated_dict.to_markdown(
        "2_data_preparation/cleaned_data/Student_grade_aggregated_data_dictionary.md",
        index=False,
    )
    print("\nGenerated Student_grade_aggregated_data_dictionary.md")

    print("\n--- Student_grade_detailed.csv Info ---")
    grade_detailed_df.info()
    print("\n--- Student_grade_detailed.csv Head ---")
    print(grade_detailed_df.head())
    detailed_dict = generate_data_dictionary(grade_detailed_df)
    detailed_dict.to_markdown(
        "2_data_preparation/cleaned_data/Student_grade_detailed_data_dictionary.md",
        index=False,
    )
    print("\nGenerated Student_grade_detailed_data_dictionary.md")

except FileNotFoundError as e:
    print(
        f"Error: {e}. Make sure the CSV files are in the '1_datasets/raw_data/' directory."
    )
