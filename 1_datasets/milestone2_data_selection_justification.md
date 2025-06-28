# Milestone 2: Data Selection Justification

This document outlines the evaluation and selection process for the primary
dataset(s) to be used in our project, "Addressing Student Engagement in Online
Learning Environments," for Milestone 2: Data Collection. Our selection is
guided by our actionable research question and the principles of data modeling
and critique discussed in the workshop.

## Our Actionable Research Question

"How do specific student interaction patterns with online course materials and
discussion forums predict academic performance and course completion rates in
online learning environments, and what interventions can be designed to improve
these metrics?"

### Datasets Evaluated

1. **Online Course Student Engagement Metrics (Kaggle) - `Courses.csv`:**
    * **Source:**  
      `https://www.kaggle.com/datasets/thedevastator/online-course-student-engagement-metrics`
    * **Initial Review:**  
      This dataset contains `Courses.csv` with columns like `course_id`,
      `userid_DI`, `registered`, `viewed`, `explored`, `certified`, `grade`,
      `start_time_DI`, `last_event_DI`, `nevents`, `ndays_act`, `nplay_video`,
      `nchapters`, `nforum_posts`, `roles`, `incomplete_flag`. It appears to be
      aggregated student data per course.
    * **Relevance to Research Question:**  
      Highly relevant. It directly provides aggregated metrics for "student
      interaction patterns" (e.g., `viewed`, `explored`, `nevents`,
      `ndays_act`, `nplay_video`, `nforum_posts`) and "academic
      performance/completion rates" (e.g., `grade`, `certified`,
      `incomplete_flag`).
    * **Data Quality/Limitations:**  
      The data seems to be at a higher level of aggregation (per user per
      course) compared to raw log data. This means some granular interaction
      details might be lost, but it offers direct measures of engagement and
      outcomes. The `_DI` suffix suggests de-identified data, which is good for
      privacy.

2. **Student Engagement Dataset (SED) - Combination of `SED_Student_log.csv`
   and user-provided grade files (`Student_activity_summary.csv`,
   `Student_grade_aggregated.csv`, `Student_grade_detailed.csv`):**
    * **Source:**  
      `https://ieeexplore.ieee.org/document/10844083/` and  
      `https://www.researchgate.net/publication/388136791_Student_Engagement_Dataset_SED_An_Online_Learning_Activity_Dataset`
    * **Initial Review:**  
      `SED_Student_log.csv` is a large CSV file (774MB) with granular log data
      (`component`, `action`, `target`, `userid`, `courseid`, `timecreated`).
      The other provided files (`Student_activity_summary.csv`,
      `Student_grade_aggregated.csv`, `Student_grade_detailed.csv`) offer
      aggregated activity and grade information.
    * **Relevance to Research Question:**  
      Extremely relevant. The `SED_Student_log.csv` provides raw data for
      "student interaction patterns," allowing for detailed feature
      engineering. The grade files directly provide "academic performance" and
      "completion rates."
    * **Data Quality/Limitations:**  
      The log data is very raw and will require substantial cleaning,
      processing, and feature engineering to derive meaningful engagement
      metrics. This offers a comprehensive exercise in data modeling from raw
      observations.

3. **Western-OC2-Lab/Student-Performance-and-Engagement-Prediction-**
   **eLearning-datasets (GitHub):**
    * **Source:**  
      `https://github.com/Western-OC2-Lab/Student-Performance-and-Engagement-Prediction-eLearning-datasets`
    * **Initial Review:**  
      This repository contains several pre-processed CSV files (`Student
      Engagement Level-Binary.csv`, `Student Engagement Level-Multiclass.csv`,
      `Student Performance Prediction-Multi.csv`, `Student Performance
      Prediction-Binary.csv`). These datasets are already structured for
      predictive tasks.
    * **Relevance to Research Question:**  
      Relevant, as they contain engineered features related to engagement and
      performance outcomes.
    * **Data Quality/Limitations:**  
      Being pre-processed, they are cleaner and potentially easier to use for
      direct modeling. However, the exact feature engineering steps are
      abstracted, limiting the exercise in raw data processing.

### Data Selection Decision and Justification

Considering our actionable research question and the Milestone 2 deliverables
that emphasize collecting, cleaning, documenting, and hosting a dataset, we
will proceed with the following primary dataset:

**Primary Dataset: Student Engagement Dataset (SED) - Combination of
`SED_Student_log.csv` and the user-provided grade/activity summary files
(`Student_activity_summary.csv`, `Student_grade_aggregated.csv`,
`Student_grade_detailed.csv`).**

* **Justification:**  
  This combination provides the most comprehensive opportunity to fulfill the
  Milestone 2 requirements. The `SED_Student_log.csv` offers granular, raw
  interaction data, which is ideal for practicing data modeling from
  observations, cleaning, and feature engineering. By combining it with the
  provided grade and activity summary files, we can link interaction patterns
  to academic performance and completion rates, directly addressing our
  research question. This dataset allows for a full demonstration of the data
  collection and preparation process, from raw data to a structured dataset
  ready for analysis.

**Secondary/Reference Dataset: Online Course Student Engagement Metrics
(Kaggle) - `Courses.csv` and
Western-OC2-Lab/Student-Performance-and-Engagement-Prediction-eLearning-datasets.**

* **Justification:**  
  These datasets will serve as valuable references. The Kaggle `Courses.csv`
  provides a good example of aggregated engagement and performance metrics,
  which can inform our feature engineering process for the SED dataset. The
  Western-OC2-Lab datasets offer examples of pre-engineered features and
  target variables for predictive modeling, providing insights for future
  analysis in Milestone 3 and helping to validate our approach to feature
  creation. They are useful for understanding different levels of data
  abstraction and preparation.
