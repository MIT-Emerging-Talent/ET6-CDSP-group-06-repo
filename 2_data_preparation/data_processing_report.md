# Data Processing Report: Student Engagement Dataset (SED)

This report details the data cleaning, preprocessing, and initial feature engineering
steps applied to the Student Engagement Dataset (SED) for Milestone 2 of the project.
The processes described herein were implemented using the
`data_cleaning_preprocessing.py` Python script.

## 1. Data Loading and Initial Cleaning

All four primary CSV files of the SED dataset were loaded into Pandas DataFrames:

* `Student_grade_detailed.csv`: Provides detailed grade information per student
  per course.
**Initial Cleaning:** A common `Unnamed: 0` column, often an artifact of CSV export
from Pandas, was identified and removed from all DataFrames to prevent redundancy
and potential issues in subsequent processing.
* `Student_grade_aggregated.csv`: Contains aggregated grade information per student.
The `SED_Student_log.csv` is the most granular and largest file, providing raw event
data. To extract meaningful insights and create features relevant to student
* **Timestamp Parsing:** The `timecreated` column was converted from an object
  (string) data type to datetime objects. This is crucial for time-series analysis
* **Date Feature Creation:** A new `date` column was extracted from the
  `timecreated` column to represent the day of the activity, enabling daily-level
* **Aggregation of User Activity Counts:** Several key engagement metrics were
  engineered by grouping the log data by `userid`:

**Initial Cleaning:** A common `Unnamed: 0` column, often an artifact of CSV export
from Pandas, was identified and removed from all DataFrames to prevent redundancy
and potential issues in subsequent processing.

### 2. Feature Engineering from `SED_Student_log.csv`

The `SED_Student_log.csv` is the most granular and largest file, providing raw
event data. To extract meaningful insights and create features relevant to student
engagement, the following steps were performed:

* **Timestamp Parsing:** The `timecreated` column was converted from an object
(string) data type to datetime objects. This is crucial for time-series analysis
and extracting time-based features.

* **Date Feature Creation:** A new `date` column was extracted from the `timecreated`
column to represent the day of the activity, enabling daily-level aggregations.

* **Aggregation of User Activity Counts:** Several key engagement metrics were
engineered by grouping the log data by `userid`:
  * **`num_days_active`:** Calculated as the number of unique days a student had
  any activity in the logs. This indicates the consistency of engagement.
  * **`total_events`:** Represents the total number of actions or events recorded
  for each student, providing a measure of overall activity volume.
  * **`num_unique_courses_accessed`:** Counts the distinct courses a student
  * **`num_forum_posts`:** Specifically counts events where the `component`
  * **`num_resource_views`:** Counts events where the `component` was
    `mod_resource` and the `action` was `viewed`, indicating consumption of
* **Handling Missing Feature Values:** After creating these new engagement
  features, any `NaN` values (which would occur for users who did not perform
  a specific action, e.g., no forum posts) were filled with `0` to ensure
  numerical consistency.
To create a comprehensive dataset for analysis, the newly engineered
engagement features from `SED_Student_log.csv` were merged with the
* The `Student_activity_summary.csv` was used as the base, as it contains a
* `Student_grade_aggregated.csv` was merged using a left join on `userid` to
* The `engagement_features` DataFrame (derived from `SED_Student_log.csv`) was
  also merged using a left join on `userid`.
**Note on `Student_grade_detailed.csv`:** This file was loaded but not directly
merged into the primary `merged_df` at this stage. It contains course-specific
grade details and would be integrated for analyses requiring a finer granularity
(e.g., predicting performance in individual courses) or could be used to
validate aggregated grades.
  * **`num_forum_posts`:** Specifically counts events where the
    `component` was `mod_forum` and the `action` was `created`,
    indicating active participation in discussions.
  * **`num_resource_views`:** Counts events where the `component`
    was `mod_resource` and the `action` was `viewed`, indicating
    consumption of course materials.

* **Handling Missing Feature Values:** After creating these new
  engagement features, any `NaN` values (which would occur for users
  who did not perform a specific action, e.g., no forum posts) were
  filled with `0` to ensure numerical consistency.

### 3. Dataset Integration

To create a comprehensive dataset for analysis, the newly engineered
engagement features from `SED_Student_log.csv` were merged with the
pre-aggregated `Student_activity_summary.csv` and
`Student_grade_aggregated.csv` files. The `userid` column served as
the primary key for these merges.

* The `Student_activity_summary.csv` was used as the base, as it
  contains a comprehensive list of `userid`s.
* `Student_grade_aggregated.csv` was merged using a left join on
  `userid` to bring in total marks and number of courses.
* The `engagement_features` DataFrame (derived from
  `SED_Student_log.csv`) was also merged using a left join on `userid`.

**Note on `Student_grade_detailed.csv`:** This file was loaded but not
directly merged into the primary `merged_df` at this stage. It contains
course-specific grade details and would be integrated for analyses
requiring a finer granularity (e.g., predicting performance in
individual courses) or could be used to validate aggregated grades.

### 4. General Cleaning and Preprocessing

After integration, general cleaning steps were applied to the
`merged_df`:

* **Data Type Conversion:** The `userid` column was explicitly
  converted to an integer type to ensure consistency.
* **Missing Value Imputation:** For numerical columns (`float64`),
  missing values were imputed with the mean of their respective
  columns. For categorical columns (`object`), missing values were
  imputed with the mode (most frequent value). This is a basic
  imputation strategy; more sophisticated methods might be explored in
  later stages.

### 5. Data Flaws and Limitations Observed

During the initial exploration and processing, the following potential
data flaws or limitations were noted:

* **Granularity of `SED_Student_log.csv`:** While highly detailed,
  extracting all possible features from this massive log file is
  computationally intensive. The current feature engineering focuses on
  common, high-level engagement indicators. Deeper analysis might
  require more complex sequence modeling or event-level feature
  extraction.
* **`Unnamed: 0` Column:** The persistent presence of this column
  across multiple CSVs indicates a common export artifact, requiring
  consistent removal.
* **Missing Values in Aggregated Data:** Although basic imputation was
  applied, the extent and patterns of missing values in the aggregated
  and grade datasets would require further investigation to ensure
  imputation does not introduce bias.
* **Definition of Engagement:** The raw log data allows for various
  interpretations of "engagement." The engineered features represent
  specific behavioral aspects, but emotional or cognitive engagement
  would require different data sources or more complex inferential
  methods.
* **Generalizability:** The datasets originate from specific online
  learning platforms/institutions. The generalizability of findings to
  all online learning environments should be considered.

### 6. Cleaned Data Output

The final processed and cleaned dataset is saved as
`0_data_collection/cleaned_sed_dataset.csv`. This file contains the
integrated and preprocessed data, ready for further exploratory data
analysis and model building in subsequent milestones.

### 7. Script for Reproduction

The entire process described in this report is encapsulated in the
`data_cleaning_preprocessing.py` script, located in the root directory
of the repository. To reproduce the `cleaned_sed_dataset.csv`, ensure
all raw SED files are in the `0_data_collection` folder and run the
script using `python data_cleaning_preprocessing.py`.
