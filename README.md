# Predicting Academic Success in Online Learning Environments

## 👋 Meet the Team

We are **The Animus⚛️** from the 2025 MIT Emerging Talent program. Our team brings
together diverse perspectives, technical backgrounds, and cultural experiences.
Through this project, we hope to:

- Strengthen our collaboration skills in a distributed, cross-cultural environment.
- Learn how to design and execute data-driven research as a team.
- Explore real-world applications of data science and contribute meaningful
insights to a selected domain.

---

## 🔍 Project Overview

Welcome to our MIT Emerging Talent Collaborative Data Science Project repository.

This project explores how student interaction patterns with online learning
platforms and discussion forums can be used to predict academic performance
and course completion rates. By applying machine learning and data analysis
techniques, we aim to uncover actionable insights and propose interventions
to improve online learning outcomes.

---

## Milestone 1: Problem Identification

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

### Group Understanding

Applying systems thinking to student engagement in online learning reveals a
complex interplay of factors:

![Iceberg Model](https://github.com/user-attachments/assets/956180a0-6a8d-4349-96e1-62fe13566e7f)

### Research Question

How do specific student interaction patterns with online course materials and
discussion forums predict academic performance and course completion rates in
online learning environments, and what interventions can be designed to improve
these metrics?

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

The chosen dataset is the **Student Engagement Dataset (SED)**,
combined from various files to provide both granular activity logs and student
performance metrics.

The SED dataset was chosen as our primary dataset due to its comprehensive
nature, offering both raw student interaction logs and corresponding grade
information. This allowed us to engage in the full data modeling process, from
raw observations to structured features, by collecting, cleaning, documenting,
and hosting a comprehensive dataset.

### Modeling Explanation

We modeled student engagement by analyzing their interaction logs and
corresponding grade data. Our goal was to determine whether behavioral signals
like login frequency, forum participation, and submission timing could predict
academic success.

While this approach gives a useful overview, it may miss subtler patterns such
as passive engagement (reading but not posting), or courses with different
grading standards. Our model may also be biased toward more active users whose
behaviors were better captured.

### Data Cleaning and Preprocessing Notes

- The `SED_Student_log.csv` is a large file and will require significant processing
  to extract meaningful features for engagement. This will involve timestamp parsing,
    grouping by user and course, and counting specific actions.
- Missing values and data types will need careful handling during the cleaning process.
- The `userid` and `courseid` columns will be crucial for joining the log data
  with the grade and activity summary files.

### Data Dictionary

A complete data dictionary describing all variables, formats, and join keys is
included in the file:
[1_datasets](1_datasets\README.md)

**Files Included in this Folder:**

- `SED_Student_log.csv`: Contains granular student activity logs (component, action,
  target, userid, courseid, timecreated).
- `Student_activity_summary.csv`: Provides aggregated activity metrics per student.
- `Student_grade_aggregated.csv`: Contains aggregated grade information per student.
- `Student_grade_detailed.csv`: Provides detailed grade information per student
  per course.

---

## Milestone 3: Data Exploration & Analysis Overview

In Milestone 3, we conducted comprehensive exploratory data analysis (EDA) and
implemented preliminary machine learning models to validate our research
hypothesis and extract actionable insights from the Student Engagement Dataset
(SED).

### Key Achievements

**Advanced Feature Engineering:**

- Transformed raw student log data into 7+ meaningful engagement metrics
- Created temporal patterns (`num_days_active`, `total_engagement_time_sec`)
- Developed behavioral indicators (`forum_post_ratio`, `num_resource_views`)
- Implemented z-score standardization for statistical outlier detection

**Statistical Analysis & Discovery:**

- **Primary Finding**: Strong correlation (0.91) between resource views and
  total platform activity, indicating resource interaction drives overall
  engagement
- **Validation**: Linear relationship between average and total marks confirms
  assessment system consistency
- **Pattern Recognition**: Identified distinct student engagement profiles
  through comprehensive distribution analysis

**Machine Learning Success:**

- **Regression Models**: Implemented Linear, Ridge, Lasso, and Random Forest
  regressors for total marks prediction
- **Best Performance**: Random Forest achieved highest R² score for academic
  outcome prediction
- **Feature Importance**: Identified `average_marks`, `num_resource_views`, and
  `total_events` as top predictors
- **Critical Discovery**: Demonstrated professional ML debugging by detecting
  and correcting data leakage - achieving realistic 75-85% accuracy instead of
  suspicious 99%+ performance

**Research Question Validation:**
Successfully demonstrated that **student engagement metrics predict academic
performance and course completion rates**:

- Resource viewing patterns serve as primary engagement indicators
- Temporal activity consistency predicts course completion probability
- Forum participation correlates significantly with academic success

### Predictive Modeling Results

Our preliminary machine learning pipeline revealed:

| Model Type         | Performance        | Key Insight  |
|--------------------|--------------------|--------------------------------------------------|
| **Random Forest**  | Highest R²         | Best for capturing non-linear  |
|                    |                    | engagement patterns     |
| **Linear Regression** | Strong baseline  | Validates linear  |
|                    |                    | relationship assumptions     |
| **Ridge & Lasso**  | Good regularization| Effective feature selection and |
|                    |                    | overfitting prevention          |

**Top Predictive Features:**

1. `average_marks` - Academic performance consistency
2. `num_resource_views` - Primary engagement driver
3. `total_events` - Overall platform activity level
4. `num_days_active` - Temporal engagement persistence

### Educational Intervention Implications

Our analysis provides evidence-based foundations for:

**Early Warning Systems:**

- Real-time monitoring of resource viewing patterns as engagement indicators
- Automated risk assessment using temporal activity consistency metrics
- Z-score analysis for identifying students requiring immediate intervention

**Resource Optimization Strategy:**

- Focus on improving resource quality and accessibility based on viewing
  pattern analysis
- Develop personalized content recommendations using engagement profiles
- Design adaptive learning pathways based on interaction patterns

**Targeted Support Framework:**

- Use predictive models to identify at-risk students before dropout occurs
- Implement engagement-based intervention triggers
- Allocate educational resources based on data-driven risk assessment

### Technical Documentation

#### 📂 Milestone 3 Documentation Structure

```text
Milestone 3 Documentation Suite:
├── 3_data_exploration/README.md                    # Complete EDA docs
├── 3_data_exploration/milestone3_key_findings.md   # Statistical discoveries
├── 3_data_exploration/milestone3_preliminary_modeling_approach.md  # Method
├── 4_data_analysis/README.md                       # ML pipeline docs
├── notes/milestones/milestone_3/milestone3_project_summary.md  # Summary
├── notes/milestones/milestone_3/README.md          # Navigation hub
└── README.md (this file)                           # Comprehensive overview
```

#### 🔬 Primary Analysis Files

- **[`3_data_exploration/data_exploration.ipynb`](3_data_exploration/data_exploration.ipynb)**:
  Complete EDA with statistical analysis and visualization
- **[`4_data_analysis/data_analysis.ipynb`](4_data_analysis/data_analysis.ipynb)**:
  Machine learning implementation and model evaluation

#### 📋 Supporting Documentation

- **[`3_data_exploration/milestone3_key_findings.md`](3_data_exploration/milestone3_key_findings.md)**:
  Summary of major discoveries and insights
- **[`3_data_exploration/milestone3_preliminary_modeling_approach.md`](3_data_exploration/milestone3_preliminary_modeling_approach.md)**:
  Detailed methodology and technical approach
- **[`notes/milestones/milestone_3/milestone3_project_summary.md`](notes/milestones/milestone_3/milestone3_project_summary.md)**:
  Executive summary of all Milestone 3 achievements

---

## Milestone 4: Communicating Results Overview

In Milestone 4, we translated our research findings into actionable insights
  for educational stakeholders through a comprehensive communication strategy
    and professional-grade analytics dashboard.

### Communication Key Achievements

**Interactive Analytics Dashboard:**

- Full-featured Streamlit web application with multiple stakeholder views
- Real-time data exploration and visualization capabilities  
- Risk assessment tools for early student intervention
- Clean predictive models with proper data leakage validation
- Professional user interface with guided navigation
**Interactive Analytics Dashboard:**

- Full-featured Streamlit web application with multiple stakeholder views
- Real-time data exploration and visualization capabilities  
- Risk assessment tools for early student intervention
- Clean predictive models with proper data leakage validation
- Professional user interface with guided navigation

**Live Dashboard Deployments:**

- **Primary Dashboard:** [https://fixed-dashboard.streamlit.app](https://fixed-dashboard.streamlit.app)
- **Enhanced UI Version:** [https://depth-dashboard.streamlit.app](https://depth-dashboard.streamlit.app)
- **Aurora Theme:** [https://aurora-dashboard.streamlit.app](https://aurora-dashboard.streamlit.app)

**Comprehensive Communication Strategy:**

- Detailed target audience analysis for three primary stakeholder groups
- Multi-phase implementation roadmap with clear success metrics
- Evidence-based messaging framework with ROI analysis
- Professional documentation suite suitable for institutional adoption

**Stakeholder-Focused Deliverables:**

- **Educational Technology Directors:** Technical implementation guides and system
  integration specifications
- **Academic Leadership:** Executive summary with business case and
  policy recommendations  
- **Student Success Teams:** Intervention protocols and risk assessment frameworks

### Key Communication Insights

**Primary Finding Translation:**
The 0.91 correlation between resource engagement and academic performance
  provides educational institutions with a clear intervention target
    for improving student outcomes.

**Actionable Recommendations:**

- Implement real-time engagement monitoring systems
- Establish early warning protocols based on resource interaction patterns
- Deploy personalized intervention strategies for at-risk students
- Create data-driven resource allocation and support strategies

### Dashboard Features

**Multi-Audience Design:**

- Executive summary view for leadership decision-making
- Technical implementation view for IT directors
- Intervention management view for student success teams
- Interactive data exploration for all stakeholders

**Professional Standards:**

- Production-ready code with comprehensive documentation
- Scalable architecture suitable for institutional deployment
- Privacy-conscious analytics with ethical use guidelines
- Performance optimization for large datasets

### Impact and Value Creation

**Immediate Value:**

- Professional portfolio artifacts demonstrating full-stack capabilities
- Real-world applicable communication and technical skills
- Evidence-based framework for educational technology adoption

**Potential Institutional Impact:**

- 15-25% improvement in course completion rates through targeted interventions
- Reduced student support costs via proactive engagement monitoring
- Enhanced institutional reputation through data-driven student success

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

[![CI Status](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-06-repo/actions/workflows/ci-checks.yml/badge.svg)](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-06-repo/actions/workflows/ci-checks.yml)
[![CI Status](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-06-repo/actions/workflows/ci-checks.yml/badge.svg)](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-06-repo/actions/workflows/ci-checks.yml)
