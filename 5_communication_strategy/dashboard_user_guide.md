# 🎓 Student Performance Analytics Dashboard - Complete User Guide

## 📋 Table of Contents

1. [Dashboard Overview]
2. [Getting Started]
3. [Navigation & Interface]
4. [Page-by-Page Guide]
5. [Data Interpretation]
6. [Troubleshooting]
7. [Best Practices]

---

## 🎯 Dashboard Overview

### Purpose

This dashboard serves as the **primary communication artifact** for Milestone 4,
  translating complex data science findings into actionable insights
    for educational stakeholders.

### Key Finding

**📊 Student engagement metrics show a 91.4% correlation with academic performance**,
  enabling early identification of at-risk students through behavioral data analysis.

### Target Audiences

- **Educational Technology Directors**: Technical implementation insights
- **Academic Affairs Leadership**: Strategic decision-making support  
- **Student Success Coordinators**: Intervention protocols and risk assessment

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install streamlit pandas plotly scikit-learn joblib
```

### Launching the Dashboard

**Access the Dashboard:**

### Primary Artifact Description

**Type:** Interactive web-based dashboard (Streamlit application)
**Deployments:**

- Primary Dashboard: [https://fixed-dashboard.streamlit.app](https://fixed-dashboard.streamlit.app)
- Enhanced UI Version: [https://depth-dashboard.streamlit.app](https://depth-dashboard.streamlit.app)
- Aurora Theme: [https://aurora-dashboard.streamlit.app](https://aurora-dashboard.streamlit.app)

### Required Files

- `cleaned_sed_dataset.csv` - Processed student engagement data
- `best_random_forest_classifier.joblib` - Pre-trained prediction model

---

## 🧭 Navigation & Interface

### Sidebar Controls

#### 🎯 Navigation

- **📊 Overview**: Executive summary and key metrics
- **📈 Analytics**: Detailed feature analysis and correlations
- **🤖 Models**: Predictive modeling and performance metrics
- **💡 Insights**: Actionable recommendations and strategies

#### 🔧 Filters

- **Risk Categories**: Filter data by student risk levels
  - **High Risk**: Total marks < 300 (Immediate intervention needed)
  - **Medium Risk**: Total marks 300-400 (Monitor closely)
  - **Low Risk**: Total marks > 400 (Performing well)

#### ℹ️ Data Info Panel

- **Records**: Total number of student records being analyzed
- **Features**: Number of engagement metrics used in analysis
- **Data Leakage**: Confirms zero data leakage in modeling

---

## 📊 Page-by-Page Guide

## 1. 📊 Overview Page

### Milestone 4 Banner

**Purpose**: Communicates the main finding and context for stakeholders

- **Key Message**: 91.4% correlation between engagement and performance
- **Visual Design**: Professional gradient with glassmorphism effects

### Key Performance Metrics (4-Card Layout)

#### Total Students

- **What it shows**: Number of student records in the filtered dataset
- **How to read**: Higher numbers indicate larger sample size for more reliable insights
- **Typical range**: 100-1000+ students depending on filters

#### Completion Rate

- **What it shows**: Percentage of students who successfully completed their courses
- **How to read**:
  - 🟢 **>80%**: Excellent retention
  - 🟡 **60-80%**: Good but room for improvement
  - 🔴 **<60%**: Concerning, needs intervention
- **Visual**: Animated progress bar with pulse effect

#### Average Score

- **What it shows**: Mean total marks across all filtered students
- **How to read**:
  - **>450**: High-performing cohort
  - **350-450**: Average performance
  - **<350**: Below-average performance

#### High Risk Percentage

- **What it shows**: Proportion of students classified as high-risk
- **How to read**:
  - 🔴 **>30%**: High concern, systematic issues
  - 🟡 **15-30%**: Normal range, targeted intervention needed
  - 🟢 **<15%**: Excellent student success rates

### Risk Distribution Visualization

#### Pie Chart (Left Column)

- **Purpose**: Shows proportional breakdown of risk categories
- **Color Coding**:
  - 🟢 **Green**: Low Risk students
  - 🟡 **Yellow**: Medium Risk students  
  - 🔴 **Red**: High Risk students
- **Interactive**: Hover to see exact counts and percentages

#### Risk Breakdown Panel (Right Column)

- **Purpose**: Numerical breakdown with exact counts
- **How to use**: Quick reference for specific numbers
- **Strategic insight**: Helps determine resource allocation needs

### Engagement Patterns Radar Chart

- **Purpose**: Compares average engagement across risk categories
- **How to read**:
  - **Larger area**: Higher engagement levels
  - **Pattern comparison**: Shows which metrics differentiate risk levels
  - **Overlay analysis**: Compare patterns across different risk groups

---

## 2. 📈 Analytics Page

### Clean Feature Analysis Tabs

#### 📝 Forum & Communication Tab

**Features Included**:

- `no_of_forum_created`: Discussion topics initiated
- `num_forum_posts`: Total posts and replies
- `forum_post_ratio`: Posts relative to total activity

**How to Interpret**:

- **High values**: Active community participants
- **Low values**: Passive learners or struggling students
- **Correlation insight**: Strong community engagement correlates with success

#### 📚 Learning Resources Tab

**Features Included**:

- `num_resource_views`: Materials accessed
- `no_of_all_files_downloaded`: Downloads completed
- `total_engagement_time_sec`: Time spent learning

**How to Interpret**:

- **Resource views**: Indicator of proactive learning behavior
- **Downloads**: Shows commitment to offline studying
- **Engagement time**: Quality metric for deep learning

#### 🎯 Course Engagement Tab

**Features Included**:

- `num_unique_courses_accessed`: Breadth of exploration
- `num_days_active`: Consistency of engagement
- `total_events`: Overall platform activity

**How to Interpret**:

- **Course diversity**: Shows curiosity and exploration
- **Active days**: Consistency predictor (more important than intensity)
- **Total events**: Overall engagement volume

#### 📋 Assessment Activity Tab

**Features Included**:

- `no_of_assignments`: Available assignments
- `number_of_quizzes`: Quiz availability
- `no_of_quizzes_attempt`: Actual quiz attempts

**How to Interpret**:

- **Assignment metrics**: Course structure indicators
- **Quiz attempts**: Shows engagement with self-assessment
- **Gap analysis**: Compare attempts vs availability

#### ⏰ Login Patterns Tab

**Features Included**:

- `weekend_login`, `weekday_login`: Temporal patterns
- `midnight_login`, `evening_login`, etc.: Time-of-day preferences
- `average_login`: Overall frequency

**How to Interpret**:

- **Weekend activity**: Indicates dedication beyond requirements
- **Time patterns**: Shows learning habits and preferences
- **Login frequency**: Consistency indicator

### Correlation Analysis

#### Correlation Heatmap

- **Purpose**: Shows relationships between all features and performance
- **Color Scale**:
  - 🔴 **Dark Red**: Strong negative correlation (-1.0 to -0.5)
  - ⚪ **White**: No correlation (around 0)
  - 🔵 **Dark Blue**: Strong positive correlation (0.5 to 1.0)
- **How to read**: Darker colors indicate stronger relationships

#### Key Correlations Table

**Columns Explained**:

- **Feature**: Engagement metric name (cleaned for readability)
- **Correlation**: Numerical correlation value (-1.0 to 1.0)
- **Strength**: Visual indicator with interpretation
  - 🔴/🟢 **Strong** (>0.5): Major predictors
  - 🟠/🟡 **Moderate** (0.3-0.5): Important factors
  - 🔵/🟦 **Weak** (0.1-0.3): Minor influences
  - ⚪ **Very Weak** (<0.1): Minimal impact
- **Direction**: Positive (more = better) or Negative (more = worse)

#### Summary Insight Cards

- **🟢 Strongest Positive Predictor**: Most powerful success indicator
- **🔴 Strongest Negative Predictor**: Warning sign metrics
- **✅ All Positive**: When all engagement leads to better outcomes

### Feature Distribution Analysis

#### Feature Selection Dropdown

- **Purpose**: Detailed analysis of individual metrics
- **Use case**: Deep-dive into specific engagement behaviors

#### Distribution Visualizations

- **Histogram**: Shows frequency distribution by risk category
- **Box Plot**: Shows median, quartiles, and outliers by risk group
- **Statistical Table**: Mean, median, standard deviation by risk

### Feature Relationship Explorer

- **Scatter Plot**: Compare any two features with risk category coloring
- **Size Mapping**: Bubble size represents total marks
- **Pattern Recognition**: Identify clusters and relationships

---

## 3. 🤖 Models Page

### Pre-Trained Model Information

#### Model Details Card

- **Algorithm**: Random Forest Classifier
- **Training**: Hyperparameter optimized
- **Features**: Number of clean engagement metrics used
- **Test Set Size**: Number of students in evaluation
- **Positive Class**: Percentage who completed courses
- **Data Leakage**: Confirmation of prevention measures

#### Performance Metrics Cards

##### Accuracy

- **Definition**: Overall correctness of predictions
- **Range**: 0.0 to 1.0 (higher is better)
- **Interpretation**:
  - **>0.90**: Excellent model performance
  - **0.80-0.90**: Good performance
  - **<0.80**: Needs improvement

##### Precision

- **Definition**: When model predicts "completion," how often it's correct
- **Formula**: True Positives / (True Positives + False Positives)
- **Business Impact**: Avoids unnecessary interventions for successful students

##### Recall

- **Definition**: Of all students who actually complete, how many are correctly identified
- **Formula**: True Positives / (True Positives + False Negatives)
- **Business Impact**: Ensures we don't miss at-risk students who need help

##### F1-Score

- **Definition**: Balanced measure combining precision and recall
- **Range**: 0.0 to 1.0 (higher is better)
- **Use case**: Single metric for overall model quality

### Confusion Matrix

**Layout**:

'''
                Predicted
              Not    Complete
           Complete
Actual Not    TN       FP
     Complete
       Complete FN    TP
'''

**Definitions**:

- **TN (True Negatives)**: Correctly identified struggling students
- **FP (False Positives)**: Incorrectly flagged successful students
- **FN (False Negatives)**: Missed at-risk students (most critical error)
- **TP (True Positives)**: Correctly identified successful students

### Classification Report Table

- **Not Completed**: Metrics for predicting struggling students
- **Completed**: Metrics for predicting successful students
- **Support**: Number of actual cases in each category

### Sample Predictions Table

**Columns**:

- **Student_ID**: Anonymized identifier
- **Probability**: Model confidence (0.0 to 1.0)
- **Prediction**: Final classification (Complete/At Risk)
- **Confidence**: Interpretation of probability
  - **High**: >0.8 or <0.2 (very confident)
  - **Medium**: 0.6-0.8 or 0.2-0.4 (moderately confident)
  - **Low**: 0.4-0.6 (uncertain, needs human review)

### Feature Importance Analysis

- **Purpose**: Shows which engagement metrics matter most for predictions
- **Horizontal Bar Chart**: Longer bars = more important features
- **Top 3 Features**: Highlighted summary of most critical metrics
- **Strategic Use**: Focus intervention programs on highest-impact behaviors

---

## 4. 💡 Insights Page

### Key Findings Section

#### Strongest Predictor Card

- **Feature**: Top correlation metric
- **Correlation Value**: Numerical strength
- **Interpretation**: What this means for student success strategies

#### Engagement Gap Analysis

- **Calculation**: Compares average engagement between high-risk and low-risk students
- **Percentage Gap**: How much more engaged successful students are
- **Strategic Insight**: Quantifies the intervention opportunity

### Actionable Strategies

#### Intervention Recommendations

- **Early Alert System**: Weekly monitoring protocols
- **Peer Support**: Mentorship program design
- **Gamification**: Engagement incentive strategies
- **Resource Promotion**: Content discovery improvements
- **Proactive Outreach**: Contact protocols for declining activity

### Summary Statistics Table

- **Comprehensive Overview**: All features with key statistics
- **Use Case**: Technical reference for detailed analysis
- **Stakeholder Value**: Supporting evidence for recommendations

---

## 📊 Data Interpretation Guide

### Understanding Risk Categories

#### High Risk (Marks < 300)

**Characteristics**:

- Low engagement across multiple metrics
- Irregular login patterns
- Minimal resource utilization
- Limited community participation

**Intervention Priority**: Immediate
**Recommended Actions**:

- Direct counselor contact within 48 hours
- Customized study plan development
- Weekly check-ins
- Peer tutoring assignment

#### Medium Risk (Marks 300-400)

**Characteristics**:

- Moderate engagement with gaps
- Inconsistent activity patterns
- Some resource usage
- Occasional community participation

**Intervention Priority**: Monitor closely
**Recommended Actions**:

- Bi-weekly progress monitoring
- Study group recommendations
- Resource usage guidance
- Motivational support

#### Low Risk (Marks > 400)

**Characteristics**:

- Consistent high engagement
- Regular login patterns
- Active resource utilization
- Strong community participation

**Intervention Priority**: Maintain momentum
**Recommended Actions**:

- Peer mentoring opportunities
- Advanced resource recommendations
- Leadership development
- Success story sharing

### Correlation Interpretation Guidelines

#### Strong Correlations (>0.5)

- **Actionable**: Direct targets for intervention
- **Reliable**: Consistent across different student populations
- **Strategic**: Foundation for policy decisions

#### Moderate Correlations (0.3-0.5)

- **Supporting**: Reinforcing factors for success
- **Contextual**: May vary by student demographics
- **Tactical**: Components of comprehensive strategies

#### Weak Correlations (0.1-0.3)

- **Supplementary**: Minor contributing factors
- **Variable**: Inconsistent across populations
- **Optional**: Lower priority for interventions

### Feature Importance Guidelines

#### Top Tier Features (>0.15 importance)

- **Resource Investment**: Prioritize system improvements
- **Training Focus**: Staff development priorities
- **Policy Development**: Core metrics for standards

#### Mid Tier Features (0.05-0.15 importance)

- **Monitoring**: Include in regular reporting
- **Enhancement**: Secondary improvement targets
- **Research**: Areas for further investigation

#### Lower Tier Features (<0.05 importance)

- **Baseline**: Maintain current functionality
- **Reporting**: Include in comprehensive dashboards
- **Future**: Potential for emerging importance

---

## 🔧 Troubleshooting

### Common Issues

#### Dashboard Won't Load

**Symptoms**: Error messages, blank screen, connection refused
**Solutions**:

1. Check file paths: Ensure `cleaned_sed_dataset.csv` is accessible
2. Verify model file: Confirm `best_random_forest_classifier.joblib` exists
3. Check dependencies: Run `pip install -r requirements.txt`
4. Browser issues: Try refreshing the deployed dashboard or using a different browser

#### Missing Data Visualizations

**Symptoms**: Empty charts, "No data available" messages
**Solutions**:

1. Check filter settings: Ensure at least one risk category is selected
2. Verify data completeness: Look for missing columns in dataset
3. Feature availability: Confirm all required features exist in data

#### Model Performance Issues

**Symptoms**: Unrealistic accuracy, error messages in Models page
**Solutions**:

1. Feature compatibility: Ensure model and data feature counts match
2. Data scaling: Verify preprocessing consistency
3. Model integrity: Reload model file if corrupted

#### Slow Performance

**Symptoms**: Long loading times, unresponsive interface
**Solutions**:

1. Data size: Consider filtering to smaller subsets
2. Browser cache: Clear cache and reload
3. Resource usage: Close other applications
4. Caching issues: Clear Streamlit cache with `Ctrl+R`

### Data Quality Checks

#### Before Analysis

- [ ] Dataset loads without errors
- [ ] All required columns present
- [ ] No excessive missing values (>10%)
- [ ] Feature engineering completed
- [ ] Data types correct

#### During Analysis

- [ ] Filters working correctly
- [ ] Visualizations displaying properly
- [ ] Correlation calculations reasonable
- [ ] Model predictions within expected ranges

#### For Stakeholder Presentation

- [ ] All pages load quickly (<5 seconds)
- [ ] Visualizations are clear and readable
- [ ] Insights are actionable and specific
- [ ] Technical details appropriate for audience

---

## 📈 Best Practices

### For Educational Technology Directors

#### Technical Analysis

1. **Focus on Models page**: Understand prediction accuracy and feature importance
2. **Data pipeline validation**: Verify data leakage prevention measures
3. **Scalability assessment**: Consider implementation across multiple institutions
4. **Integration planning**: Identify APIs and data connections needed

#### Implementation Strategy

1. **Pilot program**: Start with single department or course
2. **Baseline metrics**: Establish current performance benchmarks
3. **Staff training**: Develop user adoption programs
4. **Feedback loops**: Create continuous improvement processes

### For Academic Leadership

#### Strategic Insights

1. **Overview page focus**: Key metrics and risk distributions
2. **Correlation analysis**: Understanding engagement-performance relationships
3. **Resource allocation**: Using insights to guide budget decisions
4. **Policy implications**: Developing engagement standards and expectations

#### Communication Strategy

1. **Executive summaries**: Use key metrics for board presentations
2. **Department meetings**: Share risk distribution insights
3. **Faculty engagement**: Discuss correlation findings and implications
4. **Student success**: Align insights with retention initiatives

### For Student Success Teams

#### Operational Use

1. **Daily monitoring**: Check Overview page for current status
2. **Individual assessment**: Use Models page for specific student evaluation
3. **Intervention prioritization**: Focus on high-risk categories first
4. **Progress tracking**: Monitor changes in risk distributions over time

#### Intervention Design

1. **Evidence-based**: Use correlation insights to design programs
2. **Targeted approach**: Different strategies for different risk levels
3. **Measurable outcomes**: Track changes in engagement metrics
4. **Continuous improvement**: Adjust based on success rates

### For IT Infrastructure Teams

#### System Requirements

1. **Performance optimization**: Ensure adequate server resources
2. **Data security**: Implement appropriate access controls
3. **Backup strategies**: Protect model files and datasets
4. **Update procedures**: Plan for model retraining and data refreshes

#### User Support

1. **Access management**: Control dashboard permissions appropriately
2. **Training materials**: Develop user guides and video tutorials
3. **Help desk preparation**: Train support staff on common issues
4. **Usage monitoring**: Track adoption and identify support needs

---

## 📞 Support and Resources

### Documentation

- **Technical Setup**: See `README.md` for installation details
- **Communication Strategy**: Review `communication_strategy.md`
  for stakeholder engagement
- **Data Pipeline**: Check `data_processing_report.md` for methodology

### Contact Information

- **Technical Issues**: Project team via established communication channels
- **Strategic Questions**: Academic leadership through appropriate channels
- **Implementation Support**: Educational technology department

### Additional Resources

- **Streamlit Documentation**: <https://docs.streamlit.io/>
- **Data Science Best Practices**: Internal training materials
- **Student Success Research**: Academic literature on engagement metrics

---

**Document Version**: 1.0  
**Last Updated**: July 24, 2025  
**Dashboard Version**: Milestone 4 Final  
**Compatibility**: Streamlit 1.28+, Python 3.8+
