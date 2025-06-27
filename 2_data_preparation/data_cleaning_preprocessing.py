"""
data_cleaning_preprocessing.py

This script loads the raw Student Engagement Dataset (SED),
cleans and processes it to extract relevant engagement metrics,
and outputs a cleaned dataset for further analysis.

It merges multiple sources: activity logs, grades, and summaries,
and performs feature engineering and general preprocessing.
"""

import pandas as pd

# --- 1. Load Datasets ---
print("Loading datasets...")
log_df = pd.read_csv("1_datasets/raw_data/Student_log/SED_Student_log.csv")
activity_summary_df = pd.read_csv("1_datasets/raw_data/Student_activity_summary.csv")
grade_aggregated_df = pd.read_csv("1_datasets/raw_data/Student_grade_aggregated.csv")
grade_detailed_df = pd.read_csv("1_datasets/raw_data/Student_grade_detailed.csv")
print("Datasets loaded successfully.")

# --- 2. Initial Cleaning (Drop Unnamed: 0 columns) ---
print("Performing initial cleaning (dropping Unnamed: 0 columns)...")
for df in [log_df, activity_summary_df, grade_aggregated_df, grade_detailed_df]:
    if "Unnamed: 0" in df.columns:
        df.drop("Unnamed: 0", axis=1, inplace=True)
print("Initial cleaning complete.")

# --- 3. Feature Engineering from log_df ---
print("Starting feature engineering from SED_Student_log.csv...")

# Ensure timecreated is in datetime format
log_df["timecreated"] = pd.to_datetime(log_df["timecreated"])

# Extract date from timestamp
log_df["date"] = log_df["timecreated"].dt.date

# Calculate number of unique active days per user
days_active = log_df.groupby("userid")["date"].nunique().reset_index()
days_active.rename(columns={"date": "num_days_active"}, inplace=True)

# Total number of actions (rows) per user
total_events = log_df.groupby("userid").size().reset_index(name="total_events")

# Unique number of courses accessed per user
unique_courses_accessed = log_df.groupby("userid")["courseid"].nunique().reset_index()
unique_courses_accessed.rename(
    columns={"courseid": "num_unique_courses_accessed"}, inplace=True
)

# Forum posts created
forum_posts = log_df[
    (log_df["component"] == "mod_forum") & (log_df["action"] == "created")
]
num_forum_posts = (
    forum_posts.groupby("userid").size().reset_index(name="num_forum_posts")
)

# Resources viewed
resource_views = log_df[
    (log_df["component"] == "mod_resource") & (log_df["action"] == "viewed")
]
num_resource_views = (
    resource_views.groupby("userid").size().reset_index(name="num_resource_views")
)

# Merge all engagement features
engagement_features = pd.merge(days_active, total_events, on="userid", how="outer")
engagement_features = pd.merge(
    engagement_features, unique_courses_accessed, on="userid", how="outer"
)
engagement_features = pd.merge(
    engagement_features, num_forum_posts, on="userid", how="outer"
)
engagement_features = pd.merge(
    engagement_features, num_resource_views, on="userid", how="outer"
)

# Fill missing values with 0
engagement_features.fillna(0, inplace=True)

print("Feature engineering complete.")

# --- 4. Integrate Datasets ---
print("Integrating datasets...")

# Start from the activity summary
merged_df = activity_summary_df.copy()

# Merge aggregated grades
merged_df = pd.merge(merged_df, grade_aggregated_df, on="userid", how="left")

# Merge engineered engagement features
merged_df = pd.merge(merged_df, engagement_features, on="userid", how="left")

print("Datasets integrated successfully.")

# --- 5. General Cleaning and Preprocessing ---
print("Performing general cleaning and preprocessing...")

# Convert userid to integer type
merged_df["userid"] = merged_df["userid"].astype(int)

# Fill missing values
for col in merged_df.columns:
    if merged_df[col].dtype == "float64":
        merged_df[col].fillna(merged_df[col].mean(), inplace=True)
    elif merged_df[col].dtype == "object":
        merged_df[col].fillna(merged_df[col].mode()[0], inplace=True)

print("Cleaning complete.")

# --- 6. Save Output ---
CLEANED_DATA_PATH = "2_data_preparation/cleaned_data/cleaned_sed_dataset.csv"
merged_df.to_csv(CLEANED_DATA_PATH, index=False)
print(f"✅ Cleaned dataset saved to: {CLEANED_DATA_PATH}")

# --- 7. Summary Output ---
print("\n--- Final Merged DataFrame Info ---")
merged_df.info()
print("\n--- Final Merged DataFrame Head ---")
print(merged_df.head())

print("🎉 Script executed successfully.")
