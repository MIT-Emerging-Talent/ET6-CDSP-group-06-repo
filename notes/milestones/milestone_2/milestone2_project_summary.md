# Milestone 2: Data Collection - Project Summary and Documentation

This document provides a comprehensive overview of the activities, decisions, and
outcomes for Milestone 2: Data Collection, within the context of our project,
"Addressing Student Engagement in Online Learning Environments." It serves as
both a detailed record of our work and a resource for future presentations.

## 1. Objectives of Milestone 2

As outlined in the syllabus and the "Modeling the World Through Data" workshop,
the primary objectives for Milestone 2 were to:

* **Model our problem domain in data:** Translate the concepts of student
  engagement, academic performance, and course completion into measurable data
  points.
* **Identify relevant data:** Determine what data is necessary and relevant to
  our actionable research question.
* **Collect, clean, document, and host a dataset:** Acquire the chosen data,
  prepare it for analysis, document its characteristics, and make it accessible.

## 2. Data Selection Process

Our actionable research question guided our data selection:

> "How do specific student interaction patterns with online course materials and
> discussion forums predict academic performance and course completion rates in
> online learning environments, and what interventions can be designed to improve
> these metrics?"

We followed a structured approach for evaluating and selecting datasets, as
detailed in
[`Structured Approach for Evaluating and Selecting Datasets (Milestone 2).pdf`](../1_datasets/milestone2_data_selection_guide.pdf).
This involved:

* **Initial Screening:** Reviewing promising publicly available datasets
  identified in Milestone 1.
* **Deep Dive Evaluation:** Critiquing datasets based on relevance to our
  research question, data quality (completeness, accuracy, granularity), and
  practical considerations (volume, format, documentation).

**Selected Dataset:**

After thorough evaluation, we selected the **Student Engagement Dataset (SED)**
as our primary dataset. This dataset, comprising `SED_Student_log.csv`,
`Student_activity_summary.csv`, `Student_grade_aggregated.csv`, and
`Student_grade_detailed.csv`, offers a rich combination of granular activity logs
and student performance metrics. Our detailed justification for this selection is
documented in
[`milestone2_data_selection_justification.md`](../1_datasets/milestone2_data_selection_justification.md).

**Location of Raw Data:** The raw SED dataset files are stored in the
`1_datasets/raw_data/` subfolder.

## 3. Data Cleaning and Preprocessing

This phase involved transforming the raw data into a clean, integrated, and
analysis-ready format. The entire process is primarily encapsulated in the Python
script
[`data_cleaning_preprocessing.py`](../2_data_preparation/data_cleaning_preprocessing.py).

**Initial Data Exploration and Documentation (`explore_sed_data.py`):**

Before the main cleaning process, the `explore_sed_data.py` script was utilized
for initial data exploration and to generate data dictionaries for the raw SED
files. This script:

* **Purpose:** Served as a preliminary step to understand the structure, data
  types, unique values, and missing values within each raw dataset (e.g.,
  `SED_Student_log.csv`, `Student_activity_summary.csv`).
* **What it did:** It loaded each raw CSV file and programmatically extracted
  metadata, which was then formatted into Markdown-based data dictionaries. This
  provided a foundational understanding of the raw data's characteristics.
* **Link to Cleaning:** The insights gained from this initial exploration (e.g.,
  identifying the `Unnamed: 0` column, understanding data types, and initial
  assessment of missing values) directly informed the design and implementation
  of the more comprehensive cleaning and preprocessing steps in
  `data_cleaning_preprocessing.py`. It helped in anticipating potential issues
  and planning the necessary transformations.

**Key Steps Performed by `data_cleaning_preprocessing.py`:**

* **Data Loading and Initial Cleaning:** All four SED CSV files were loaded.
  Initial cleaning involved removing the `Unnamed: 0` index column from each
  DataFrame.
* **Feature Engineering from `SED_Student_log.csv`:** This was a critical step
  due to the large, granular nature of the log file. We extracted several key
  engagement features:
  * **Timestamp Parsing:** Converted `timecreated` to datetime objects.
  * **`num_days_active`:** Number of unique days a student was active.
  * **`total_events`:** Total number of actions recorded for each student.
  * **`num_unique_courses_accessed`:** Number of distinct courses a student
    interacted with.
  * **`num_forum_posts`:** Count of forum posts created by each student.
  * **`num_resource_views`:** Count of resources viewed by each student.
  * `NaN` values for these new features (where a user didn't perform an action)
    were filled with `0`.
* **Dataset Integration:** The newly engineered engagement features were merged
  with `Student_activity_summary.csv` and `Student_grade_aggregated.csv` using
  `userid` as the key. This created a comprehensive `merged_df`.
* **General Cleaning and Preprocessing:**
  * `userid` column was converted to integer type.
  * Missing numerical values were imputed with the mean, and categorical values
    with the mode (a basic imputation strategy).

**Detailed Documentation:** A comprehensive explanation of these steps,
including the rationale and specific transformations, is provided in
[`data_processing_report.md`](../2_data_preparation/data_processing_report.md).

**Location of Cleaned Data:** The final processed and cleaned dataset,
`cleaned_sed_dataset.csv`, is saved in the
`2_data_preparation/cleaned_data/` subfolder.

## 4. Data Documentation

Thorough documentation is crucial for reproducibility and understanding. We have
created:

* **Data Dictionaries:** Initial data dictionaries for all raw SED files are
  included in the [`README.md`](../1_datasets/README.md) of the `1_datasets`
  folder and the [`README.md`](../2_data_preparation/README.md) of the
  `2_data_preparation` folder.
* **Data Processing Report:** As mentioned,
  [`data_processing_report.md`](../2_data_preparation/data_processing_report.md)
  details the cleaning and feature engineering process.

## 5. Retrospective and Learning

At the conclusion of Milestone 2, our team conducted a retrospective to reflect
on our processes, successes, and areas for improvement. This reflection is
documented in
[`2_data_collection.md`](../collaboration/retrospectives/2_data_collection.md).

## 6. Key Concepts and Guides

Throughout Milestone 2, we referred to several guiding documents:

* [`Key Concepts from “Modeling the World Through Data” Workshop (June 17).pdf`](./milestones/milestone2/Key%20Concepts%20from%20%E2%80%9CModeling%20the%20World%20Through%20Data%E2%80%9D%20Workshop%20(June%2017).pdf):
  Outlines key concepts from the "Modeling the World Through Data" workshop.
* [`milestone2_concepts_appendix.md`](milestone2_concepts_appendix.md): A
  detailed appendix of terms and methodologies relevant to data collection.
* [`To-Do List - Milestone 2- Data Collection.pdf`](./milestones/milestone2/To-Do%20List%20-%20Milestone%202-%20Data%20Collection.pdf):
  Our detailed checklist for Milestone 2 tasks.

## 7. Next Steps

With the data collected, cleaned, and documented, our team is now prepared to
move into Milestone 3: Data Exploration and Analysis, where we will delve deeper
into the cleaned dataset to extract insights and build models to answer our
research question.
