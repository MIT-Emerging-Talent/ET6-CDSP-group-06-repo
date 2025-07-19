
# Milestone 3: Preliminary Modeling Approach

This document outlines the preliminary modeling approach adopted for Milestone 3:
Data Exploration and Analysis. Building upon the insights gained from
comprehensive Exploratory Data Analysis (EDA), this phase demonstrates the
predictive power of engagement metrics on academic outcomes through systematic
machine learning applications.

## Research Question Reminder

"How do specific student interaction patterns with online course materials and
discussion forums predict academic performance and course completion rates in
online learning environments, and what interventions can be designed to improve
these metrics?"

## Modeling Objectives

Based on our research question and EDA findings, we identified two primary
modeling objectives:

1. **Predict Academic Performance**: Regression analysis to predict continuous
   total marks based on engagement and behavioral metrics
2. **Predict Course Completion**: Binary classification to determine course
   completion probability from early engagement indicators

## Data Preparation for Modeling

### Dataset Foundation

The analysis used the fully processed `cleaned_sed_dataset.csv` that includes:

- **Original features**: From activity summary, grade aggregated, and grade
  detailed datasets
- **Engineered features**: Temporal engagement metrics, behavioral ratios, and
  interaction patterns
- **Statistical features**: Z-score normalized variables for outlier detection

### Feature Selection Strategy

We selected **25+ features** spanning multiple engagement dimensions:

**Academic Indicators**:

- `average_marks`, `number_of_quizzes_completed`, `no_of_assignments`

**Engagement Metrics**:

- `total_events`, `num_resource_views`, `num_days_active`, `num_forum_posts`

**Behavioral Patterns**:

- Login timing patterns (`weekend_login`, `evening_login`, etc.)
- Course interaction metrics (`no_of_viewed_courses`,
  `num_unique_courses_accessed`)

**Statistical Features**:

- Z-score normalized versions of key metrics for outlier detection

### Data Quality Assurance

- **Missing Value Handling**: Filled with 0 (representing non-engagement)
- **Infinite Value Processing**: Replaced with 0 to prevent computational errors
- **Data Type Consistency**: Ensured all features are numeric for ML algorithms
- **Train-Test Split**: 80/20 split with random_state=7 for reproducibility

## Model Implementation

### 1. Regression Analysis: Total Marks Prediction

#### Model Selection Rationale

We implemented four complementary regression approaches:

**Linear Regression**:

- **Purpose**: Establish baseline linear relationship performance
- **Advantage**: Highly interpretable coefficients
- **Assumption**: Linear relationship between features and target

**Random Forest Regressor**:

- **Purpose**: Capture non-linear patterns and feature interactions
- **Advantage**: Handles complex relationships automatically
- **Capability**: Provides feature importance rankings

**Ridge Regression (L2 Regularization)**:

- **Purpose**: Prevent overfitting through coefficient shrinkage
- **Advantage**: Maintains all features while reducing impact of less important
  ones
- **Parameter**: alpha=1.0 for moderate regularization

**Lasso Regression (L1 Regularization)**:

- **Purpose**: Automatic feature selection through coefficient zeroing
- **Advantage**: Identifies most important features by eliminating others
- **Parameter**: alpha=0.1 for balanced selection

#### Model Performance Results

**Performance Summary**:

| Model | MSE | R² Score | Interpretation |
|-------|-----|----------|----------------|
| Random Forest | Lowest | Highest | Best overall performance |
| Linear Regression | Moderate | Good | Strong baseline |
| Ridge Regression | Moderate | Good | Effective regularization |
| Lasso Regression | Moderate | Good | Feature selection insights |

#### Feature Importance Analysis

**Top 5 Predictive Features (Random Forest)**:

1. **`average_marks`** - Strongest individual academic predictor
2. **`num_resource_views`** - Primary engagement-based predictor  
3. **`total_events`** - Overall platform activity measure
4. **`num_days_active`** - Temporal engagement consistency
5. **Quiz completion metrics** - Academic engagement indicators

### 2. Classification Analysis: Course Completion Prediction

#### Binary Target Creation

We created the `course_completed` binary variable using a data-driven threshold:

- **Threshold**: 443 total marks (based on statistical analysis)
- **Class 0**: Course not completed (< 443 marks)
- **Class 1**: Course completed (≥ 443 marks)

#### Model Approach

**Logistic Regression** was selected for course completion prediction due to:

- **Interpretability**: Clear understanding of feature impact on completion
  probability
- **Baseline Performance**: Standard approach for binary classification
- **Coefficient Analysis**: Direct insight into engagement metric influence

## Key Findings and Insights

### 1. **Engagement Metrics Are Predictive**

Our models successfully demonstrate that engagement metrics can predict academic
outcomes with reasonable accuracy, validating our core research hypothesis.

### 2. **Resource Viewing Dominance**

The strong performance of `num_resource_views` as a predictor confirms our EDA
finding that resource interaction is the primary driver of engagement.

### 3. **Multi-Dimensional Engagement**

The inclusion of temporal (`num_days_active`), volume (`total_events`), and
behavioral (`forum_posts`) metrics provides a comprehensive engagement profile.

### 4. **Academic Performance Hierarchy**

`average_marks` remains the strongest predictor, indicating that past academic
performance is the most reliable indicator of future performance.

## Model Validation and Limitations

### Validation Approach

- **Single Split Validation**: 80/20 train-test split for initial assessment
- **Consistent Random State**: Reproducible results across model comparisons
- **Multiple Metrics**: MSE and R² for comprehensive performance evaluation

### Current Limitations

1. **Single Validation Split**: No cross-validation for robust performance
   estimation
2. **No Hyperparameter Tuning**: Default parameters used for all models
3. **Limited Feature Engineering**: Basic feature selection without advanced
   techniques
4. **Class Imbalance**: Potential issues in course completion classification

### Areas for Improvement (Milestone 4)

1. **Cross-Validation**: Implement k-fold cross-validation for robust evaluation
2. **Hyperparameter Optimization**: Grid search or random search for parameter
   tuning
3. **Feature Selection**: Advanced techniques like recursive feature elimination
4. **Ensemble Methods**: Combine models for improved prediction accuracy
5. **Advanced Evaluation**: Precision, recall, F1-score for classification tasks

## Implications for Educational Interventions

### 1. **Early Warning System Design**

The predictive capability of engagement metrics enables:

- **Real-time Monitoring**: Track resource viewing patterns as primary indicator
- **Risk Assessment**: Use temporal activity patterns for dropout prediction
- **Automated Alerts**: Trigger interventions based on engagement thresholds

### 2. **Resource Optimization Strategy**

The dominance of resource-related features suggests:

- **Content Quality Focus**: Improve resource accessibility and relevance
- **Personalized Recommendations**: Adapt content based on engagement patterns
- **Interaction Design**: Optimize resource presentation for maximum engagement

### 3. **Targeted Support Framework**

Model insights inform intervention design:

- **High-Risk Identification**: Students with low engagement scores require
  immediate attention
- **Personalized Interventions**: Tailor support based on specific engagement
  deficits
- **Success Prediction**: Allocate resources to students most likely to benefit

## Technical Implementation Notes

### Code Organization

The modeling implementation follows best practices:

- **Modular Approach**: Separate data preparation, model training, and
  evaluation
- **Consistent Methodology**: Standardized approach across all models
- **Reproducible Results**: Fixed random states for consistent outcomes
- **Clear Documentation**: Extensive comments explaining each step

### Performance Considerations

- **Feature Scaling**: Z-score normalization handles different feature scales
- **Memory Efficiency**: Optimized data loading and processing
- **Computational Cost**: Random Forest most expensive, Linear Regression most
  efficient

## Connection to Project Goals

This preliminary modeling phase successfully:

1. **Validates Research Question**: Demonstrates predictive relationship between
   engagement and outcomes
2. **Establishes Baseline Performance**: Creates foundation for advanced
   modeling in Milestone 4
3. **Identifies Key Predictors**: Guides intervention strategy development
4. **Proves Concept Viability**: Shows feasibility of engagement-based
   prediction systems

---

*This modeling approach establishes the foundation for advanced model
development and intervention strategy design in subsequent project phases.*

- `engagement_score` (composite score of various activities)
- `forum_posts` (number of posts in discussion forums)
- `time_spent_lectures_min` (total time spent on lecture materials)
- `quiz_score` (performance on quizzes, as a strong indicator of understanding)
- **Target (Dependent Variable - y):** `course_completed`
- **Evaluation Metrics:**
  - **Accuracy:** Overall correctness of predictions.
  - **Precision, Recall, F1-score:** To assess the model's performance on both completed
    and not-completed classes, especially important if one class is imbalanced.
  - **Confusion Matrix:** To visualize the types of correct and incorrect predictions.

### 2. Predicting Academic Performance: Linear Regression

- **Objective:** To predict a student's final grade (`final_grade` - continuous numerical
  value).
- **Model Choice:** **Linear Regression**.
  - **Justification:** Linear Regression is a fundamental algorithm for predicting
    continuous outcomes. It provides a straightforward way to model the linear
    relationship between our chosen features and the final grade, offering interpretability
    regarding how each engagement metric contributes to the academic performance.
- **Features (Independent Variables - X):**
  - `engagement_score`
  - `forum_posts`
  - `time_spent_lectures_min`
  - `quiz_score`
- **Target (Dependent Variable - y):** `final_grade`
- **Evaluation Metrics:**
  - **Mean Squared Error (MSE) / Root Mean Squared Error (RMSE):** To measure the
    average magnitude of the errors.
  - **R-squared:** To indicate the proportion of the variance in the dependent variable
    that is predictable from the independent variables.

## Model Training and Evaluation Process

For both models, the standard machine learning workflow was followed:

1. **Data Splitting:** The dataset was split into training and testing sets
   (e.g., 80% training, 20% testing) to evaluate the model's performance on
   unseen data.

2. **Model Training:** The chosen models (Logistic Regression and Linear Regression)
   were trained on the training set.

3. **Evaluation:** Performance metrics (as listed above) were calculated to
   assess the models' effectiveness.
This preliminary modeling phase is expected to provide initial evidence of the
predictive power of engagement metrics. The insights gained will inform further
analysis and potentially more complex modeling in subsequent milestones. The
interpretability of these models will be crucial for suggesting actionable
interventions, directly addressing the latter part of our research question.

Future work will involve exploring more advanced algorithms, feature engineering,
and cross-validation techniques to improve model robustness and generalization.
robustness and generalization.
