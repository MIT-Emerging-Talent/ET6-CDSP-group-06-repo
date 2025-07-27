# 📦 1_datasets: Data Collection and Selection

This folder houses the raw datasets identified and selected for our project,
"Addressing Student Engagement in Online Learning Environments," as part of
Milestone 2: Data Collection. It also contains documentation detailing our data
selection process.

## Raw Datasets

The following raw datasets have been collected and are stored in the
`raw_data/` subfolder:

* `SED_Student_log.csv`: Granular log data of student activities.
* `Student_activity_summary.csv`: Aggregated activity metrics per student.
* `Student_grade_aggregated.csv`: Aggregated grade information per student.
* `Student_grade_detailed.csv`: Detailed grade information per student per course.

### Data Dictionaries

Below are the data dictionaries for the files in this dataset, outlining column
  names, data types, unique values, and missing values. These serve as initial
    documentation for understanding the dataset.

| Column Name | Data Type | Unique Values | Missing Values | Description |
|:------------|:----------|--------------:|---------------:|:------------|
| Unnamed: 0 | int64 | 12139424 | 0 | Index column from original CSV. |
| component | object | 36 | 0 | The Moodle component involved in the activity  |
| action | object | 37 | 0 | The specific action performed by the user  |
| target | object | 74 | 0 | The specific item or context of the action |
| userid | int64 | 16128 | 0 | Unique identifier for the student. |
| courseid | int64 | 2826 | 0 | Unique identifier for the course. |
| timecreated | object | 6040037 | 0 | Timestamp of when the activity occurred. |

#### `Student_activity_summary.csv` Data Dictionary

| Column Name | Data Type | Unique Values | Missing Values | Description |
|:------------|:----------|--------------:|---------------:|:------------|
| `Unnamed: 0` | int64 | 16128 | 0 | Index column from original CSV. |
| `userid` | float64 | 16128 | 0 | Unique identifier for the student. |
| `number_of_courses` | float64 | 10 | 0 | # of courses students enrolled in. |
| `average_marks` | float64 | 1589 | 0 | Average obtained - across all courses. |
| `average_login` | float64 | 1024 | 0 | Average number of logins. |
| `weekend_login` | float64 | 291 | 0 | Average # of logins during weekends. |
| `weekday_login` | float64 | 948 | 0 | Average # of logins during weekdays. |
| `midnight_login` | float64 | 344 | 0 | Average # of logins during midnight. |
| `early_morning_login` | float64 | 291 | 0 | Average #  logins early morning |
| `late_morning_login` | float64 | 291 | 0 | Average # of logins late morning |
| `afternoon_login` | float64 | 344 | 0 | Average nu#mber of logins  afternoon. |
| `evening_login` | float64 | 102 | 0 | Average # of logins during evening. |
| `night_login` | float64 | 102 | 0 | Average number of logins during night |
| `no_of_viewed_courses` | float64 | 1148 | 0 | Average # of courses viewed. |
| `no_of_attendance_taken` | float64 | 102 | 0 | Average # attendances taken. |
| `no_of_all_files_downloaded` | float64 | 102 | 0 | Avg # files downloaded. |
| `no_of_assignments` | float64 | 102 | 0 | Avg # of assignments submitted. |
| `no_of_forum_created` | float64 | 102 | 0 | Average # of forum posts created. |
| `number_of_quizzes` | float64 | 102 | 0 | Average # of quizzes available. |
| `no_of_quizzes_completed` | float64 | 102 | 0 | Average # of quizzes compl. |
| `no_of_quizzes_attempt` | float64 | 102 | 0 | Average # of quizzes attempted. |

#### `Student_grade_aggregated.csv` Data Dictionary

| Column Name | Data Type | Unique Values | Missing Values | Description |
|:------------|:----------|--------------:|---------------:|:------------|
| `Unnamed: 0` | int64 | 16128 | 0 | Index column from original CSV. |
| `userid` | int64 | 16128 | 0 | Unique identifier for the student. |
| `number_of_courses` | float64 | 10 | 0 | # of courses the student is enrolled in.|
| `total_marks` | float64 | 1589 | 0 | Total marks obtained across all courses.|

#### `Student_grade_detailed.csv` Data Dictionary

| Column Name | Data Type | Unique Values | Missing Values | Description |
|:------------|:----------|--------------:|---------------:|:------------|
| `Unnamed: 0` | int64 | 16609 | 0 | Index column from original CSV. |
| `userid` | int64 | 16128 | 0 | Unique identifier for the student. |
| `courseid` | int64 | 2826 | 0 | Unique identifier for the course. |
| `formatted agreed mark` | object | 1589 | 0 | Formatted agreed mark for the course.|
| `actual grade` | object | 10 | 0 | Actual letter grade for the course. |
| `faculty` | object | 10 | 0 | Faculty the course belongs to. |

### Data Cleaning and Preprocessing Notes

* The `SED_Student_log.csv` is a large file and will require significant processing
  to extract meaningful features for engagement. This will involve timestamp parsing,
    grouping by user and course, and counting specific actions.
* Missing values and data types will need careful handling during the cleaning process.
* The `userid` and `courseid` columns will be crucial for joining the log data
  with the grade and activity summary files.

### Data Selection Process

Our team evaluated several publicly available datasets to identify the most
suitable one for our actionable research question. The detailed evaluation
criteria and the justification for our final selection can be found in the
following document:

* [`milestone2_data_selection_justification.md`](milestone2_data_selection_justification.md):
  This document outlines the evaluation process and provides the rationale for
  choosing the Student Engagement Dataset (SED) as our primary dataset.

### Guides

* [`guide.md`](1_datasets/guide.md): This guide provides
  further instructions and context for working with datasets in this phase.
