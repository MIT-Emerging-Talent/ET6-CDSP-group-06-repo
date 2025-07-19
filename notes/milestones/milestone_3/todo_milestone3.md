# To-Do List: Milestone 3 - Data Exploration and Analysis

This to-do list breaks down the structured approach for Milestone 3 into actionable
tasks. Work through these items with your team to ensure a comprehensive data
exploration and analysis phase.

## Phase 3: Data Exploration and Analysis

### **Objective:** Transform cleaned data into actionable knowledge, uncover patterns

test hypotheses, and build preliminary models to address the research question

### **Deliverables:**

* Exploratory Data Analysis (EDA) Notebooks (`.ipynb`)
* Key Findings Summary (`.md`)
* Preliminary Modeling Approach (`.md`)
* Milestone 3 Retrospective (`.md`)

#### **Step 1: Initial Data Loading and Sanity Checks**

* [ ] Load `cleaned_sed_dataset.csv` into a Jupyter Notebook.
* [ ] Display the first few rows (`df.head()`).
* [ ] Check data types and non-null values (`df.info()`).
* [ ] Get basic descriptive statistics (`df.describe()`).
* [ ] Verify the number of rows and columns.

#### **Step 2: Univariate Analysis**

* [ ] For **Categorical Variables**:
  * [ ] Count unique values (`value_counts()`).
  * [ ] Visualize distributions using bar plots.
* [ ] For **Numerical Variables**:
  * [ ] Visualize distributions using histograms and box plots.
  * [ ] Calculate measures of central tendency (mean, median, mode) and
    dispersion (standard deviation, variance, quartiles).
  * [ ] Identify outliers.

#### **Step 3: Bivariate and Multivariate Analysis**

* [ ] Conduct **Correlation Analysis**:
  * [ ] Calculate correlation matrices for numerical variables.
  * [ ] Visualize correlations using heatmaps.
* [ ] Explore **Relationship between Categorical and Numerical Variables**:
  * [ ] Use box plots or violin plots to compare numerical distributions across
    different categories.
* [ ] Explore **Relationship between Categorical Variables**:
  * [ ] Use cross-tabulations and stacked bar plots.
* [ ] Perform **Feature Engineering** (if necessary): Create new features from
  existing ones that might better capture underlying patterns.

#### **Step 4: Hypothesis Testing and Statistical Inference**

* [ ] **Formulate Hypotheses** based on your research question and initial
  observations.
* [ ] **Choose Appropriate Statistical Tests** (e.g., t-tests, ANOVA, chi-square
  tests, regression analysis) based on the type of variables and hypotheses.
* [ ] **Execute Statistical Tests** in your notebook.
* [ ] **Interpret Results:** Understand p-values, confidence intervals, and effect
  sizes.

#### **Step 5: Preliminary Modeling**

* [ ] **Define Target Variable** (e.g., academic performance, course completion).
* [ ] **Select Features** for your model.
* [ ] **Choose Model Type** (e.g., linear regression, logistic regression,
  decision trees, simple clustering).
* [ ] **Train and Evaluate Model:** Split data, train, and evaluate performance
  using appropriate metrics.
* [ ] **Iterate:** Refine features or model choice based on initial results.

#### **Step 6: Interpretation and Documentation**

* [ ] **Narrative in Notebooks:** Add explanations, insights, and interpretations
  directly within your Jupyter notebooks.
* [ ] **Key Findings Summary:** Create a separate Markdown document summarizing
  the most significant discoveries, patterns, and relationships.
* [ ] **Preliminary Modeling Approach Document:** Detail your chosen modeling
  approach, rationale, and initial results.

#### **Step 7: Ethical Considerations and Limitations**

* [ ] Review your analysis for **Bias Detection**.
* [ ] Clearly state the **Generalizability** and scope of your findings.
* [ ] Reiterate considerations for **Privacy**.
* [ ] Frame conclusions in terms of **Confidence vs. Truth**.

#### **Finalization and Submission Preparation (Phase 4)**

* [ ] Create the **Milestone 3 Retrospective**.
* [ ] Update the **main `README.md`** with Milestone 3 progress and outcomes.
* [ ] Organize all files in the GitHub repository according to the specified
  structure.
* [ ] Create the `milestone3-submission` Git tag.
* [ ] Complete the Milestone 3 survey.
* [ ] Update the **main `README.md`** with Milestone 3 progress and outcomes.
* [ ] Organize all files in the GitHub repository according to the specified structure.
