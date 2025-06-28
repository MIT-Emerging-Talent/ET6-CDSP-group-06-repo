# 🛠️ 2_data_preparation: Data Cleaning and Preprocessing

This folder contains the scripts and documentation related to the cleaning,
preprocessing, and initial feature engineering of our selected dataset for
Milestone 2.

## Scripts and Reports

* [`explore_sed_data.py`](explore_sed_data.py):
  * **Purpose:** This Python script was used for initial data exploration of the
    raw Student Engagement Dataset (SED) files. It helps in understanding the
    raw data structure, data types, unique values, and missing values by
    generating data dictionaries for each component of the SED dataset.
  * **Input:** Reads raw data from `1_datasets/raw_data/` (specifically
    `SED_Student_log.csv`, `Student_activity_summary.csv`,
    `Student_grade_aggregated.csv`, `Student_grade_detailed.csv`).
  * **Output:** Generates Markdown files (`_data_dictionary.md`) containing data
    dictionaries for each input CSV.

* [`data_cleaning_preprocessing.py`](data_cleaning_preprocessing.py):
  * **Purpose:** This Python script performs the core data cleaning and
    preprocessing steps on the raw Student Engagement Dataset (SED) files. It
    handles initial data loading, drops unnecessary columns, engineers new
    engagement features from the `SED_Student_log.csv` (such as
    `num_days_active`, `total_events`, `num_unique_courses_accessed`,
    `num_forum_posts`, `num_resource_views`), integrates the various SED
    components, and applies general cleaning (e.g., handling missing values).
  * **Input:** Reads raw data from `1_datasets/raw_data/`.
  * **Output:** Generates `cleaned_sed_dataset.csv` and saves it to
    `2_data_preparation/cleaned_data/`.

* [`data_processing_report.md`](data_processing_report.md):
  * **Purpose:** This Markdown document provides a detailed explanation of the
    data cleaning, preprocessing, and initial feature engineering steps executed
    by the `data_cleaning_preprocessing.py` script. It covers timestamp
    parsing, activity aggregation, dataset merging, handling of missing values,
    and discusses observed data flaws and limitations.

### Cleaned Data Output

The processed and cleaned dataset, ready for exploration and analysis, is
located in the `cleaned_data/` subfolder:

* `cleaned_sed_dataset.csv`: The integrated and preprocessed dataset derived
  from the raw SED files.

### Guides

* [`guide.md`](2_data_preparation/guide.md): This
  guide provides further instructions and context for data preparation
  activities.
