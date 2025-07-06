# ET6 Collaborative Data Science Project – Group 06

[![CI Status](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-06-repo/actions/workflows/ci-checks.yml/badge.svg)](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-06-repo/actions/workflows/ci-checks.yml)

Welcome to our MIT Emerging Talent Collaborative Data Science Project repository.

This project explores how data science, collaboration, and domain expertise
intersect to solve real-world problems. We are currently
in **Milestone 3: Data Exploration and Analysis**, focused on exploring our
cleaned dataset, performing predictive modeling, and evaluating how student
engagement patterns relate to academic performance.

---

## 👋 Meet the Team

We are **The Animus⚛️** from the 2025 MIT Emerging Talent program. Our team brings
together diverse perspectives, technical backgrounds, and cultural experiences.
Through this project, we hope to:

- Strengthen our collaboration skills in a distributed, cross-cultural environment
- Learn how to design and execute data-driven research as a team
- Explore real-world applications of data science and contribute meaningful
insights to a selected domain

Our domain of interest will be defined in Milestone 1.

---

## 🔍 Project Overview

- **Track:** Collaborative Data Science Project (CDSP)
- **Team:** The Animus⚛️
- **Domain of Interest:** Education
- **Timeline:** May–August 2025
- **Status:** 🚧 Exploring (Milestone 3)

---

## 🎯 Milestone 1: Problem Identification

### Problem Statement

In the era of increasingly prevalent online learning, maintaining student
engagement has become a significant challenge. Many students, particularly in
self-paced or asynchronous online courses, struggle with motivation, timely
completion of assignments, and active participation. This leads to higher
dropout rates and reduced learning outcomes. This problem is exacerbated by the
lack of immediate feedback and personalized interaction often present in
traditional classroom settings. From a personal perspective, many of us have
experienced the isolation and difficulty in staying focused when learning
remotely, especially when faced with distractions or a lack of direct
accountability.

### Group Understanding (Systems Thinking)

Applying systems thinking to student engagement in online learning reveals a
complex interplay of factors:

- **Events:** Missed deadlines, low forum participation, minimal login activity.
- **Patterns:** Decline in activity after initial weeks, higher disengagement in
  self-paced courses.
- **Structures:** Course design flaws, platform limitations, instructor pedagogy,
  socio-economic factors.
- **Mental Models:** Student beliefs about self-discipline, instructor
  assumptions about autonomy.

### Actionable Research Question

#### Research Question

How do specific student interaction patterns with online course materials and
discussion forums predict academic performance and course completion rates in
online learning environments, and what interventions can be designed to improve
these metrics?

This question is:

- **Specific:** Focuses on interaction patterns and measurable outcomes.
- **Achievable:** Uses accessible LMS data (logins, forum activity, grades).
- **Actionable:** Findings can inform interventions like automated nudges or
  course redesigns.

### Key Stakeholders  

- **Students**: Primary users; their engagement behaviors directly impact
  outcomes.
- **Instructors**: Design courses and interventions (e.g., forum prompts,
  feedback).
- **LMS Providers**: Can implement platform changes (e.g., gamification,
  analytics).
- **Institutions**: Set policies (e.g., enrollment caps, support services).
- **Policymakers**: Fund infrastructure (e.g., broadband access for
  underserved students).
For detailed stakeholder analysis, see: [Stakeholder Breakdown](0_domain_study/stakeholders.md).

---

## Milestone 2: Data Collection Overview

This folder contains the primary dataset selected for our project, "Addressing
Student Engagement in Online Learning Environments," as part of Milestone 2:
Data Collection. The chosen dataset is the **Student Engagement Dataset (SED)**,
combined from various files to provide both granular activity logs and student
performance metrics.

The SED dataset was chosen as our primary dataset due to its comprehensive
nature, offering both raw student interaction logs and corresponding grade
information. This allows us to fulfill the Milestone 2 requirements of
collecting, cleaning, documenting, and hosting a dataset by engaging in the full
data modeling process—from raw observations to structured features. It directly
supports our actionable research question by providing the necessary data on
student interaction patterns, academic performance, and course completion rates.

**Files Included in this Folder:**

- `SED_Student_log.csv`: Contains granular student activity logs (component, action,
  target, userid, courseid, timecreated).
- `Student_activity_summary.csv`: Provides aggregated activity metrics per student.
- `Student_grade_aggregated.csv`: Contains aggregated grade information per student.
- `Student_grade_detailed.csv`: Provides detailed grade information per student
  per course.

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

- The `SED_Student_log.csv` is a large file and will require significant processing
  to extract meaningful features for engagement. This will involve timestamp parsing,
    grouping by user and course, and counting specific actions.
- Missing values and data types will need careful handling during the cleaning process.
- The `userid` and `courseid` columns will be crucial for joining the log data
  with the grade and activity summary files.

### Next Steps for Data Preparation

1. **Feature Engineering from `SED_Student_log.csv`:**  
   Transform raw log data into features representing student interaction patterns
   (e.g., total logins, time spent, forum activity counts, resource access  
   frequency).

2. **Data Integration:**  
   Join the engineered features from `SED_Student_log.csv` with  
   `Student_activity_summary.csv`, `Student_grade_aggregated.csv`, and  
   `Student_grade_detailed.csv` using `userid` and `courseid`.

3. **Final Cleaning and Validation:**  
   Address any remaining missing values, outliers, and inconsistencies in the  
   combined dataset.

4. **Final Data Dictionary:**  
   Create a comprehensive data dictionary for the final, cleaned, and integrated
   dataset.

## Milestone 3: Data Exploration and Analysis

We explored and modeled the cleaned Student Engagement Dataset (SED) to address
our research question about how student interaction patterns predict academic
performance.

### Non-Technical Explanation of Our Findings

We analyzed data on online student activity to understand whether patterns of
engagement can help predict academic performance.

#### Key Findings

- Students who log in more frequently, participate in forums, and complete
assignments tend to achieve higher marks.

- This suggests that consistent, active engagement is linked to better
academic outcomes in online learning environments.

#### Visual Evidence

#### Scatter Plots of Engagement Features vs. Average Marks

![Scatterplots of Engagement Features](https://github.com/user-attachments/assets/2019a625-9e07-46e8-b9d6-5ce5251be465)

> The scatter plots show positive trends between average marks and:
>
> - Days active
> - Total events
> - Forum posts
> - Number of assignments

These relationships suggest that students with more consistent activity tend to
score higher.

#### Correlation Heatmap

![Correlation Heatmap](https://github.com/user-attachments/assets/389f0f9d-0315-4e53-b8df-77385a6db3b4)

> The heatmap shows strong positive correlations among key engagement features,
> supporting their predictive value for academic performance.

#### Prediction Accuracy

- Our simple regression model explains about **69%** of the variation
in student marks.
- This means engagement patterns provide meaningful predictive power.

#### Sources of Error or Uncertainty

- Unmeasured factors like motivation or prior knowledge.
- Limits of our linear model (it may not capture all complexity).
- Data quality and accuracy of online logs.

#### What Does This Mean?

- Online learning platforms could use engagement data to identify students at
risk of underperforming.
- Instructors can intervene early, offering support or feedback to improve outcomes.

### Technical Description of Our Analysis and Results

We aimed to answer: **Can online engagement patterns predict academic performance?**

**Analysis steps:**

#### Exploratory Data Analysis (EDA)

- Inspected missing values, distributions, and outliers.
- Visualized relationships using:
  - **Scatter plots** between average marks and key engagement metrics
  (e.g. days active, forum posts).
  - **Correlation heatmaps** to detect linear relationships among features.

- EDA helps understand data structure, find potential predictors, and check for
multicollinearity.

#### Feature Selection & Engineering

- Chose variables capturing:
  - Logins by time of day/week
  - Forum activity
  - Assignments submitted
  - Overall events
- Dropped redundant or index columns.

- We focused on measurable, meaningful engagement metrics relevant to instructors
and LMS systems.

#### Modeling Approach

- Applied **Linear Regression**:
  - Split data (80% train / 20% test).
  - Fitted model on training set.
  - Evaluated using **Mean Squared Error (106.68)** and **R-squared (0.69)**.

**Why Linear Regression?**

- Interpretable coefficients.
- Good first step to assess linear relationships.
- Easy to communicate findings.

#### Evaluation

- **Residual Plots**:
  - Showed some spread, suggesting imperfect fit and possible heteroscedasticity.
- **Coefficients Analysis**:
  - Identified important features (e.g., total_events, no_of_assignments, forum posts).

**Possible flaws in our analysis:**

- **Linearity assumption** may not hold for all relationships.
- **No interaction terms** or non-linear effects captured.
- **Potential overfitting** despite test evaluation.
- **Feature engineering scope** limited to simple counts.

**Conclusion:**  
Our linear regression model provides a solid baseline, explaining 69% of
variance in average marks using straightforward engagement features. Future
iterations can improve predictive power and interpretability by adopting more
advanced modeling techniques.

### Reproducibility

All data, notebooks, and scripts necessary to replicate this analysis are
included in:

- /1_datasets/
- /3_data_exploration/
- /4_data_analysis/

Please see these folders to run the full analysis pipeline using our cleaned dataset.

---

## 📁 Repository Structure

```bash
.
/
├── README.md                   # Project overview and main findings
├── /collaboration/             # Team norms, strategies, and retrospectives
├── /notes/                     # Shared resources and learning materials
├── /0_domain_study/            # Domain research and background
├── /1_datasets/                # Raw and processed datasets
├── /2_data_preparation/        # Scripts for cleaning and processing data
├── /3_data_exploration/        # Scripts for initial data understanding
├── /4_data_analysis/           # Scripts for in-depth analysis
├── /5_communication_strategy/  # Materials for communicating findings
└── /6_final_presentation/      # Final presentation materials
```

---

## 🧑‍🤝‍🧑 Collaboration Foundation

- 🔹 [Group Norms](collaboration/guide/1_group_norms.md)
- 🔹 [Communication Plan](collaboration/communication.md)
- 🔹 [Constraints](collaboration/constraints.md)
- 🔹 [Learning Goals](collaboration/learning_goals.md)
- 🔹 [Retrospective](collaboration/retrospectives)

---

## 🗓️ Project Milestones

| Milestone | Focus                        | Status        | Due Date   |
|----------|------------------------------|---------------|------------|
| 0        | Cross-Cultural Collaboration | 🟢 Done | June 2     |
| 1        | Problem Identification        | 🟢 Done    | June 16    |
| 2        | Data Collection               | 🟢 Done   | June 30    |
| 3        | Data Analysis                 | 🟢 Done    | July 21    |
| 4        | Communicating Results         | ⏳ Upcoming    | August 11  |
| 5        | Final Presentation            | ⏳ Upcoming    | August 25  |

---

## 🚀 Getting Started (For Contributors)

```bash
git clone https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-06-repo.git
cd ET6-CDSP-group-06-repo
```

---

## 👥 Team Members

- [Caesar](https://github.com/CaesarGhazi) ➡️
- [Fahed](https://github.com/RandomProjects-db) ➡️
- [Tomas](https://github.com/Sufi-to) ➡️
- [Terry](https://github.com/terryekoe) ➡️
- [Mohamed](https://github.com/MohammadRAlSalloum) ➡️
- [Maria](https://github.com/MaRia19280) ➡️

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> “Coming together is a beginning. Keeping together is progress. Working together
is success.” – Henry Ford
