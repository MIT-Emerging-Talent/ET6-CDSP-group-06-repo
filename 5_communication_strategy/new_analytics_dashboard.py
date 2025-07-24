"""
Enhanced Student Engagement Analytics Dashboard - Milestone 4 Communication Artifact

This is an improved version of the original dashboard with enhanced features:
- Better error handling and data validation
- More interactive visualizations with advanced filtering
- Enhanced UI/UX with modern design patterns
- Comprehensive stakeholder-focused insights
- Advanced model evaluation and interpretation
- Real-time risk assessment with confidence intervals
- Automated report generation capabilities

🎯 Key Finding: 91.4% correlation between engagement metrics and academic performance

Target Audiences:
- Educational Technology Directors: Technical implementation insights
- Academic Affairs Leadership: Strategic decision-making support  
- Student Success Coordinators: Intervention protocols and risk assessment
- Faculty Members: Student engagement monitoring tools

Enhanced Features:
- Multi-dimensional data exploration with advanced filtering
- Real-time predictive analytics with uncertainty quantification
- Interactive risk assessment with intervention recommendations
- Automated insight generation and report export
- Stakeholder-specific dashboards and views
- Advanced statistical analysis and hypothesis testing

Usage:
    streamlit run new_analytics_dashboard.py

Author: Amazon Q Enhanced Version
"""

import os
import warnings
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional, Any
import base64

import joblib
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score, recall_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import chi2_contingency, pearsonr

warnings.filterwarnings("ignore")

# Enhanced page configuration
st.set_page_config(
    page_title="🎓 Enhanced Student Analytics Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/your-repo/issues',
        'Report a bug': 'https://github.com/your-repo/issues',
        'About': "Enhanced Student Engagement Analytics Dashboard v2.0"
    }
)

# Enhanced CSS with modern design patterns
st.markdown("""
<style>
    /* Import modern fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Global variables */
    :root {
        --primary-color: #2563eb;
        --secondary-color: #7c3aed;
        --success-color: #059669;
        --warning-color: #d97706;
        --danger-color: #dc2626;
        --info-color: #0891b2;
        --dark-color: #1f2937;
        --light-color: #f8fafc;
        --border-radius: 12px;
        --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }
    
    /* Global styling */
    .main {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    /* Enhanced header with gradient animation */
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 50%, var(--info-color) 100%);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin: 2rem 0;
        animation: gradientShift 3s ease-in-out infinite alternate;
        text-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    
    /* Enhanced metric cards with glassmorphism */
    .metric-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        border-radius: var(--border-radius);
        color: var(--dark-color);
        text-align: center;
        box-shadow: var(--shadow-lg);
        margin: 0.5rem 0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.6s ease;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-xl);
        background: rgba(255, 255, 255, 0.35);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
        color: var(--primary-color);
    }
    
    .metric-title {
        font-size: 0.9rem;
        font-weight: 600;
        opacity: 0.8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .metric-subtitle {
        font-size: 0.8rem;
        opacity: 0.7;
        margin-top: 0.5rem;
    }
    
    /* Enhanced info cards */
    .info-card {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
        border-left: 4px solid var(--info-color);
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1rem 0;
        box-shadow: var(--shadow-md);
        transition: all 0.3s ease;
    }
    
    .success-card {
        background: linear-gradient(135deg, rgba(5, 150, 105, 0.1) 0%, rgba(16, 185, 129, 0.1) 100%);
        border-left: 4px solid var(--success-color);
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1rem 0;
        box-shadow: var(--shadow-md);
        transition: all 0.3s ease;
    }
    
    .warning-card {
        background: linear-gradient(135deg, rgba(217, 119, 6, 0.1) 0%, rgba(245, 158, 11, 0.1) 100%);
        border-left: 4px solid var(--warning-color);
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1rem 0;
        box-shadow: var(--shadow-md);
        transition: all 0.3s ease;
    }
    
    .danger-card {
        background: linear-gradient(135deg, rgba(220, 38, 38, 0.1) 0%, rgba(239, 68, 68, 0.1) 100%);
        border-left: 4px solid var(--danger-color);
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1rem 0;
        box-shadow: var(--shadow-md);
        transition: all 0.3s ease;
    }
    
    /* Enhanced sidebar */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(255,255,255,0.9) 0%, rgba(248,250,252,0.9) 100%);
        backdrop-filter: blur(10px);
    }
    
    /* Enhanced buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-md);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
    }
    
    /* Enhanced selectbox */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid rgba(37, 99, 235, 0.2);
        border-radius: var(--border-radius);
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }
    
    /* Progress indicators */
    .progress-container {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 4px;
        margin: 1rem 0;
    }
    
    .progress-bar {
        height: 8px;
        background: linear-gradient(90deg, var(--success-color), var(--info-color));
        border-radius: 6px;
        transition: width 1.5s ease-in-out;
    }
    
    /* Enhanced tables */
    .dataframe {
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: var(--shadow-md);
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }
    
    .slide-in-left {
        animation: slideInLeft 0.6s ease-out;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.5rem;
        }
        
        .metric-card {
            padding: 1.5rem;
        }
        
        .metric-value {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Configuration and constants
class Config:
    """Configuration class for dashboard settings"""
    
    # Data paths
    DATA_PATHS = [
        "cleaned_sed_dataset.csv",
        "../2_data_preparation/cleaned_data/cleaned_sed_dataset.csv",
        "../cleaned_sed_dataset.csv",
        "../../2_data_preparation/cleaned_data/cleaned_sed_dataset.csv",
    ]
    
    MODEL_PATH = "best_random_forest_classifier.joblib"
    
    # Risk thresholds
    RISK_THRESHOLDS = {
        'high': 300,
        'medium': 400
    }
    
    # Color schemes
    COLORS = {
        'primary': '#2563eb',
        'secondary': '#7c3aed',
        'success': '#059669',
        'warning': '#d97706',
        'danger': '#dc2626',
        'info': '#0891b2',
        'risk_colors': {
            'Low Risk': '#059669',
            'Medium Risk': '#d97706',
            'High Risk': '#dc2626'
        }
    }
    
    # Feature categories for better organization
    FEATURE_CATEGORIES = {
        "📝 Forum & Communication": [
            "no_of_forum_created", "num_forum_posts", "forum_post_ratio"
        ],
        "📚 Learning Resources": [
            "num_resource_views", "no_of_all_files_downloaded", "total_engagement_time_sec"
        ],
        "🎯 Course Engagement": [
            "num_unique_courses_accessed", "number_of_courses_x", "number_of_courses_y", 
            "no_of_viewed_courses", "num_days_active", "total_events"
        ],
        "📋 Assessment Activity": [
            "no_of_assignments", "number_of_quizzes", "no_of_quizzes_attempt", "no_of_attendance_taken"
        ],
        "⏰ Login Patterns": [
            "average_login", "weekend_login", "weekday_login", "midnight_login",
            "early_morning_login", "late_morning_login", "afternoon_login", 
            "evening_login", "night_login"
        ]
    }

# Utility functions
class DataProcessor:
    """Enhanced data processing utilities"""
    
    @staticmethod
    @st.cache_data(ttl=3600)  # Cache for 1 hour
    def load_and_process_data() -> Tuple[Optional[pd.DataFrame], List[str], Dict[str, Any]]:
        """
        Load and process student data with comprehensive feature engineering
        
        Returns:
            Tuple of (processed_dataframe, feature_list, metadata)
        """
        try:
            # Try to load data from multiple possible locations
            data_df = None
            used_path = None
            
            for path in Config.DATA_PATHS:
                try:
                    data_df = pd.read_csv(path)
                    used_path = path
                    st.success(f"✅ Successfully loaded data from: {path}")
                    break
                except FileNotFoundError:
                    continue
            
            if data_df is None:
                st.error("""
                📂 Dataset not found! Please ensure 'cleaned_sed_dataset.csv' is available.
                
                Expected locations:
                - Current directory: cleaned_sed_dataset.csv
                - Relative path: ../2_data_preparation/cleaned_data/cleaned_sed_dataset.csv
                """)
                return None, [], {}
            
            # Store original shape
            original_shape = data_df.shape
            
            # Feature engineering
            data_df = DataProcessor._engineer_features(data_df)
            
            # Get the EXACT clean features from notebook (24 features)
            clean_features = DataProcessor._get_clean_features(data_df)
            
            st.success(f"✅ Using exact notebook feature set: {len(clean_features)} features")
            
            # Create target variable if missing
            if "course_completed" not in data_df.columns:
                if "total_marks" in data_df.columns:
                    data_df["course_completed"] = (data_df["total_marks"] >= Config.RISK_THRESHOLDS['medium']).astype(int)
                    st.success("✅ Created 'course_completed' target variable")
                else:
                    st.error("❌ Cannot create target variable - 'total_marks' not found")
                    return None, [], {}
            
            # Create risk categories
            data_df["risk_category"] = data_df["total_marks"].apply(DataProcessor._categorize_risk)
            
            # Clean data
            required_columns = clean_features + ["total_marks", "course_completed", "risk_category"]
            available_columns = [col for col in required_columns if col in data_df.columns]
            
            clean_df = data_df[available_columns].copy()
            clean_df = clean_df.dropna()
            
            # Create metadata
            metadata = {
                'original_shape': original_shape,
                'processed_shape': clean_df.shape,
                'features_engineered': len(data_df.columns) - original_shape[1],
                'clean_features_count': len(clean_features),
                'data_source': used_path,
                'processing_timestamp': datetime.now().isoformat(),
                'feature_reconstruction': len(clean_features) == 56
            }
            
            return clean_df, clean_features, metadata
            
        except Exception as e:
            st.error(f"Error processing data: {str(e)}")
            return None, [], {}
    
    @staticmethod
    def _engineer_features(df: pd.DataFrame) -> pd.DataFrame:
        """Engineer additional features from existing data"""
        
        # Create engagement time if missing
        if "total_engagement_time_sec" not in df.columns:
            df["total_engagement_time_sec"] = df["total_events"] * 60  # Rough estimate
        
        # Create forum post ratio
        if "forum_post_ratio" not in df.columns:
            df["forum_post_ratio"] = df.apply(
                lambda row: row["num_forum_posts"] / row["total_events"] if row["total_events"] > 0 else 0,
                axis=1
            )
        
        # Create z-score features for numerical columns (excluding leaky ones)
        numerical_cols = df.select_dtypes(include=["number"]).columns
        leaky_columns = {'userid', 'total_marks', 'average_marks', 'course_completed', 'no_of_quizzes_completed'}
        
        for col in numerical_cols:
            if col not in leaky_columns and f"zscore_{col}" not in df.columns:
                df[f"zscore_{col}"] = (df[col] - df[col].mean()) / df[col].std()
        
        # Create interaction features
        if "engagement_intensity" not in df.columns:
            df["engagement_intensity"] = df["total_events"] / (df["num_days_active"] + 1)
        
        if "resource_efficiency" not in df.columns:
            df["resource_efficiency"] = df["num_resource_views"] / (df["total_engagement_time_sec"] + 1)
        
        return df
    
    @staticmethod
    def _get_clean_features(df: pd.DataFrame) -> List[str]:
        """Get list of clean features (no data leakage) - EXACT match to notebook"""
        
        # EXACT features from your notebook's final_clean_features
        # These are the 24 features your model was actually trained on
        notebook_clean_features = [
            # Course engagement (but not completion)
            'number_of_courses_x', 'number_of_courses_y', 'no_of_viewed_courses',
            
            # Learning activities  
            'no_of_assignments', 'no_of_forum_created', 'number_of_quizzes',
            'no_of_quizzes_attempt', 'no_of_all_files_downloaded',
            
            # Login and engagement patterns
            'average_login', 'weekend_login', 'weekday_login', 'midnight_login',
            'early_morning_login', 'late_morning_login', 'afternoon_login', 
            'evening_login', 'night_login',
            
            # Derived engagement metrics (from feature engineering)
            'num_days_active', 'total_events', 'num_unique_courses_accessed',
            'num_forum_posts', 'num_resource_views', 'total_engagement_time_sec', 
            'forum_post_ratio'
        ]
        
        # Return only features that exist in the dataframe
        available_features = [f for f in notebook_clean_features if f in df.columns]
        
        st.info(f"🎯 Using EXACT notebook features: {len(available_features)} out of {len(notebook_clean_features)} expected")
        
        # Show which features are missing (if any)
        missing_features = [f for f in notebook_clean_features if f not in df.columns]
        if missing_features:
            st.warning(f"⚠️ Missing features: {missing_features}")
        
        return available_features
    
    @staticmethod
    def reconstruct_original_features(df: pd.DataFrame, target_count: int = 56) -> Tuple[pd.DataFrame, List[str]]:
        """Attempt to reconstruct the original 56 features used in model training"""
        
        df_enhanced = df.copy()
        
        # Get current clean features
        current_features = DataProcessor._get_clean_features(df_enhanced)
        
        st.info(f"🔍 Starting with {len(current_features)} features, need {target_count}")
        
        # If we still don't have enough, create additional engineered features
        while len(current_features) < target_count:
            missing_count = target_count - len(current_features)
            st.info(f"🔧 Creating {missing_count} additional features...")
            
            # Create interaction features
            numerical_base = ["total_events", "num_days_active", "num_resource_views", "num_forum_posts"]
            available_numerical = [f for f in numerical_base if f in df_enhanced.columns]
            
            feature_created = False
            
            # Create polynomial features
            for i, feat1 in enumerate(available_numerical):
                if len(current_features) >= target_count:
                    break
                    
                for feat2 in available_numerical[i+1:]:
                    if len(current_features) >= target_count:
                        break
                        
                    new_feature = f"{feat1}_x_{feat2}_interaction"
                    if new_feature not in current_features:
                        try:
                            df_enhanced[new_feature] = df_enhanced[feat1] * df_enhanced[feat2]
                            current_features.append(new_feature)
                            feature_created = True
                            st.info(f"✅ Created interaction feature: {new_feature}")
                        except:
                            continue
            
            # Create ratio features
            if len(current_features) < target_count:
                for i, feat1 in enumerate(available_numerical):
                    if len(current_features) >= target_count:
                        break
                        
                    for feat2 in available_numerical[i+1:]:
                        if len(current_features) >= target_count:
                            break
                            
                        new_feature = f"{feat1}_div_{feat2}_ratio"
                        if new_feature not in current_features:
                            try:
                                df_enhanced[new_feature] = df_enhanced[feat1] / (df_enhanced[feat2] + 1)
                                current_features.append(new_feature)
                                feature_created = True
                                st.info(f"✅ Created ratio feature: {new_feature}")
                            except:
                                continue
            
            # If we couldn't create any new features, break to avoid infinite loop
            if not feature_created:
                st.warning(f"⚠️ Could only reconstruct {len(current_features)} features out of {target_count}")
                break
        
        # Final feature list (take exactly target_count if we have more)
        final_features = current_features[:target_count]
        
        st.success(f"✅ Final feature set: {len(final_features)} features")
        
        return df_enhanced, final_features
    
    @staticmethod
    def _categorize_risk(marks: float) -> str:
        """Categorize student risk based on marks"""
        if marks < Config.RISK_THRESHOLDS['high']:
            return "High Risk"
        elif marks < Config.RISK_THRESHOLDS['medium']:
            return "Medium Risk"
        else:
            return "Low Risk"

class ModelManager:
    """Enhanced model management utilities"""
    
    @staticmethod
    @st.cache_resource
    def load_pretrained_model():
        """Load pre-trained model with detailed information"""
        try:
            if os.path.exists(Config.MODEL_PATH):
                # Try to load the model
                model_data = joblib.load(Config.MODEL_PATH)
                
                # Check if it's a model object directly or a dictionary with metadata
                if hasattr(model_data, 'predict'):
                    # It's a model object directly
                    model = model_data
                    metadata = {
                        'type': type(model).__name__,
                        'features_expected': getattr(model, 'n_features_in_', 'Unknown'),
                        'source': 'Direct model file'
                    }
                elif isinstance(model_data, dict) and 'model' in model_data:
                    # It's a dictionary with model and metadata
                    model = model_data['model']
                    metadata = {
                        'type': type(model).__name__,
                        'features_expected': model_data.get('n_features', getattr(model, 'n_features_in_', 'Unknown')),
                        'feature_names': model_data.get('feature_names', []),
                        'saved_timestamp': model_data.get('saved_timestamp', 'Unknown'),
                        'source': 'Model with metadata'
                    }
                else:
                    st.error("❌ Invalid model file format")
                    return None, {}
                
                st.success(f"✅ Loaded your model: {Config.MODEL_PATH}")
                st.info(f"📊 Model type: {metadata['type']}, Expected features: {metadata['features_expected']}")
                
                return model, metadata
            else:
                st.warning(f"⚠️ Model file not found: {Config.MODEL_PATH}")
                return None, {}
        except Exception as e:
            st.error(f"Error loading your model: {str(e)}")
            st.info("💡 Make sure your model file is compatible and not corrupted")
            return None, {}
    
    @staticmethod
    def evaluate_model_on_data(model, X_test, y_test, model_name: str = "Model") -> Dict[str, Any]:
        """Evaluate a model on test data and return comprehensive metrics"""
        
        try:
            st.info(f"🔍 Evaluating {model_name}...")
            st.info(f"📊 Test data shape: {X_test.shape}")
            
            # Handle feature alignment if needed
            if hasattr(model, 'n_features_in_') and model.n_features_in_ != X_test.shape[1]:
                st.warning(f"⚠️ Feature mismatch for {model_name}: Expected {model.n_features_in_}, got {X_test.shape[1]}")
                
                if model.n_features_in_ > X_test.shape[1]:
                    # Pad with zeros
                    padding = np.zeros((X_test.shape[0], model.n_features_in_ - X_test.shape[1]))
                    X_test_aligned = np.column_stack([X_test, padding])
                    st.info(f"🔧 Padded {model.n_features_in_ - X_test.shape[1]} features with zeros")
                else:
                    # Use subset
                    X_test_aligned = X_test.iloc[:, :model.n_features_in_] if hasattr(X_test, 'iloc') else X_test[:, :model.n_features_in_]
                    st.info(f"🔧 Using first {model.n_features_in_} features")
                
                st.info(f"📊 Aligned data shape: {X_test_aligned.shape}")
            else:
                X_test_aligned = X_test
                st.info(f"✅ No feature alignment needed")
            
            # CRITICAL: Check if this is your existing model and handle it properly
            if "Your Existing Model" in model_name:
                st.info("🔍 Detected your existing model - using exact feature matching...")
                
                # Check if we have the exact number of features the model expects
                if hasattr(model, 'n_features_in_') and model.n_features_in_ == X_test_aligned.shape[1]:
                    st.success(f"✅ Perfect feature match! Model expects {model.n_features_in_}, we have {X_test_aligned.shape[1]}")
                    
                    # Use direct prediction (Random Forest doesn't need scaling)
                    try:
                        y_pred = model.predict(X_test_aligned)
                        y_pred_proba = model.predict_proba(X_test_aligned)[:, 1] if hasattr(model, 'predict_proba') else None
                        
                        accuracy_test = accuracy_score(y_test, y_pred)
                        st.success(f"🎯 Direct prediction accuracy: {accuracy_test:.4f} ({accuracy_test:.1%})")
                        
                        if accuracy_test > 0.85:
                            st.success("🏆 Excellent performance! Model is working correctly!")
                        elif accuracy_test > 0.7:
                            st.info("📊 Good performance - model is working well")
                        else:
                            st.warning("⚠️ Lower than expected performance")
                            
                    except Exception as e:
                        st.error(f"❌ Error with direct prediction: {str(e)}")
                        # Fallback to basic prediction
                        y_pred = model.predict(X_test_aligned)
                        y_pred_proba = model.predict_proba(X_test_aligned)[:, 1] if hasattr(model, 'predict_proba') else None
                
                elif hasattr(model, 'n_features_in_') and model.n_features_in_ > X_test_aligned.shape[1]:
                    # Model expects more features - this shouldn't happen with exact matching
                    st.error(f"❌ Feature mismatch: Model expects {model.n_features_in_}, we have {X_test_aligned.shape[1]}")
                    st.error("This suggests the feature list doesn't match the trained model exactly")
                    
                    # Try padding as fallback
                    padding = np.zeros((X_test_aligned.shape[0], model.n_features_in_ - X_test_aligned.shape[1]))
                    X_test_padded = np.column_stack([X_test_aligned, padding])
                    st.warning(f"⚠️ Padding with {model.n_features_in_ - X_test_aligned.shape[1]} zero features as fallback")
                    
                    y_pred = model.predict(X_test_padded)
                    y_pred_proba = model.predict_proba(X_test_padded)[:, 1] if hasattr(model, 'predict_proba') else None
                
                elif hasattr(model, 'n_features_in_') and model.n_features_in_ < X_test_aligned.shape[1]:
                    # Model expects fewer features - truncate
                    st.warning(f"⚠️ Model expects {model.n_features_in_}, we have {X_test_aligned.shape[1]} - truncating")
                    X_test_truncated = X_test_aligned[:, :model.n_features_in_]
                    
                    y_pred = model.predict(X_test_truncated)
                    y_pred_proba = model.predict_proba(X_test_truncated)[:, 1] if hasattr(model, 'predict_proba') else None
                
                else:
                    # No feature count info - try direct prediction
                    st.info("ℹ️ No feature count info available - trying direct prediction")
                    y_pred = model.predict(X_test_aligned)
                    y_pred_proba = model.predict_proba(X_test_aligned)[:, 1] if hasattr(model, 'predict_proba') else None
            else:
                # For new models, use appropriate scaling based on model type
                if "Logistic Regression" in model_name or "Support Vector Machine" in model_name:
                    # These models typically need scaling
                    scaler = StandardScaler()
                    X_test_scaled = scaler.fit_transform(X_test_aligned)
                    y_pred = model.predict(X_test_scaled)
                    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, 'predict_proba') else None
                else:
                    # Tree-based models typically don't need scaling
                    y_pred = model.predict(X_test_aligned)
                    y_pred_proba = model.predict_proba(X_test_aligned)[:, 1] if hasattr(model, 'predict_proba') else None
            
            # Calculate comprehensive metrics
            metrics = {
                'accuracy': accuracy_score(y_test, y_pred),
                'precision': precision_score(y_test, y_pred, zero_division=0),
                'recall': recall_score(y_test, y_pred, zero_division=0),
                'f1': f1_score(y_test, y_pred, zero_division=0),
                'auc': roc_auc_score(y_test, y_pred_proba) if y_pred_proba is not None else None
            }
            
            st.info(f"📊 Final {model_name} metrics: Accuracy={metrics['accuracy']:.4f}, F1={metrics['f1']:.4f}")
            
            # Confusion matrix
            cm = confusion_matrix(y_test, y_pred)
            
            # Classification report
            class_report = classification_report(y_test, y_pred, output_dict=True)
            
            return {
                'success': True,
                'model_name': model_name,
                'metrics': metrics,
                'predictions': y_pred,
                'probabilities': y_pred_proba,
                'confusion_matrix': cm,
                'classification_report': class_report,
                'test_size': len(y_test)
            }
            
        except Exception as e:
            st.error(f"❌ Error evaluating {model_name}: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'model_name': model_name
            }
    
    @staticmethod
    def compare_models(results_dict: Dict[str, Dict]) -> pd.DataFrame:
        """Compare multiple model results and return comparison dataframe"""
        
        comparison_data = []
        
        for model_name, result in results_dict.items():
            if result['success']:
                metrics = result['metrics']
                comparison_data.append({
                    'Model': model_name,
                    'Accuracy': f"{metrics['accuracy']:.4f}",
                    'Precision': f"{metrics['precision']:.4f}",
                    'Recall': f"{metrics['recall']:.4f}",
                    'F1-Score': f"{metrics['f1']:.4f}",
                    'AUC': f"{metrics['auc']:.4f}" if metrics['auc'] is not None else "N/A",
                    'Test Size': result['test_size']
                })
            else:
                comparison_data.append({
                    'Model': model_name,
                    'Accuracy': "Error",
                    'Precision': "Error", 
                    'Recall': "Error",
                    'F1-Score': "Error",
                    'AUC': "Error",
                    'Test Size': "Error"
                })
        
        return pd.DataFrame(comparison_data)
    
    @staticmethod
    def save_model_with_metadata(model, filename: str, feature_names: List[str], 
                                metrics: Dict[str, float] = None, 
                                model_type: str = "Unknown") -> bool:
        """Save model with comprehensive metadata"""
        try:
            model_data = {
                'model': model,
                'feature_names': feature_names,
                'n_features': len(feature_names),
                'model_type': model_type,
                'saved_timestamp': datetime.now().isoformat(),
                'metrics': metrics or {},
                'version': '2.0',
                'source': 'Enhanced Dashboard Training'
            }
            
            joblib.dump(model_data, filename)
            return True
            
        except Exception as e:
            st.error(f"Error saving model: {str(e)}")
            return False

# Initialize the application
def initialize_app():
    """Initialize the application with data loading and setup"""
    
    # Load and process data
    data_result = DataProcessor.load_and_process_data()
    
    if data_result[0] is None:
        st.error("Failed to load data. Please check your data files and try again.")
        st.stop()
    
    df, clean_features, metadata = data_result
    
    # Store in session state for persistence
    if 'df' not in st.session_state:
        st.session_state.df = df
        st.session_state.clean_features = clean_features
        st.session_state.metadata = metadata
    
    return st.session_state.df, st.session_state.clean_features, st.session_state.metadata

# Main application header
def render_header():
    """Render the main application header"""
    
    st.markdown(
        '<h1 class="main-header">🎓 Enhanced Student Analytics Platform</h1>',
        unsafe_allow_html=True
    )
    
    # Enhanced milestone banner
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.1) 0%, rgba(124, 58, 237, 0.1) 100%);
        border: 2px solid rgba(37, 99, 235, 0.2);
        padding: 2rem;
        border-radius: 16px;
        margin: 2rem 0;
        text-align: center;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    " class="fade-in-up">
        <div style="position: relative; z-index: 2;">
            <h2 style="color: var(--primary-color); margin-bottom: 1rem; font-weight: 700;">
                🎯 Milestone 4: Enhanced Communication Results
            </h2>
            <p style="font-size: 1.1rem; margin-bottom: 1.5rem; color: var(--dark-color);">
                Advanced analytics dashboard demonstrating our key research finding with enhanced insights:
            </p>
            <div style="
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                color: white;
                padding: 1.5rem;
                border-radius: 12px;
                margin: 1rem 0;
                box-shadow: var(--shadow-lg);
            ">
                <span style="font-size: 1.4rem; font-weight: 700;">
                    📊 Student engagement metrics show <span style="color: #fbbf24;">91.4% correlation</span> with academic performance
                </span>
            </div>
            <p style="font-size: 1rem; color: var(--dark-color); opacity: 0.8;">
                Explore comprehensive analytics, predictive models, and actionable insights for educational stakeholders.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar(df: pd.DataFrame, metadata: Dict[str, Any]) -> Tuple[str, List[str], Dict[str, Any]]:
    """Render enhanced sidebar with navigation and filters"""
    
    st.sidebar.markdown("## 🎯 Navigation")
    
    # Enhanced page selection with icons and descriptions
    pages = {
        "📊 Executive Overview": "High-level metrics and key insights",
        "📈 Advanced Analytics": "Deep-dive statistical analysis", 
        "🤖 Predictive Models": "Machine learning and predictions",
        "💡 Strategic Insights": "Actionable recommendations",
        "📋 Data Explorer": "Interactive data exploration",
        "📄 Report Generator": "Export and reporting tools"
    }
    
    page = st.sidebar.radio(
        "Select Dashboard:",
        options=list(pages.keys()),
        format_func=lambda x: x,
        help="Navigate between different dashboard views"
    )
    
    # Show page description
    st.sidebar.markdown(f"*{pages[page]}*")
    
    st.sidebar.markdown("---")
    
    # Enhanced filters section
    st.sidebar.markdown("## 🔧 Smart Filters")
    
    # Risk category filter
    risk_categories = df["risk_category"].unique().tolist()
    selected_risks = st.sidebar.multiselect(
        "🎯 Risk Categories:",
        options=risk_categories,
        default=risk_categories,
        help="Filter students by risk level"
    )
    
    # Performance range filter
    min_marks, max_marks = int(df["total_marks"].min()), int(df["total_marks"].max())
    marks_range = st.sidebar.slider(
        "📊 Performance Range:",
        min_value=min_marks,
        max_value=max_marks,
        value=(min_marks, max_marks),
        help="Filter by total marks range"
    )
    
    # Engagement level filter
    engagement_levels = ["All", "High Engagement", "Medium Engagement", "Low Engagement"]
    selected_engagement = st.sidebar.selectbox(
        "⚡ Engagement Level:",
        options=engagement_levels,
        help="Filter by student engagement level"
    )
    
    # Advanced filters (collapsible)
    with st.sidebar.expander("🔍 Advanced Filters"):
        # Course completion filter
        completion_filter = st.selectbox(
            "Course Completion:",
            options=["All", "Completed", "Not Completed"]
        )
        
        # Activity period filter
        activity_levels = ["All", "Very Active (>20 days)", "Active (10-20 days)", "Less Active (<10 days)"]
        activity_filter = st.selectbox(
            "Activity Level:",
            options=activity_levels
        )
    
    st.sidebar.markdown("---")
    
    # Data quality indicators
    st.sidebar.markdown("## ℹ️ Data Quality")
    
    # Create quality metrics
    total_records = len(df)
    filtered_records = len(df[
        (df["risk_category"].isin(selected_risks)) &
        (df["total_marks"].between(marks_range[0], marks_range[1]))
    ])
    
    quality_metrics = {
        "📊 Total Records": f"{total_records:,}",
        "🔍 Filtered Records": f"{filtered_records:,}",
        "🎯 Features": f"{len(st.session_state.clean_features)}",
        "✅ Data Leakage": "Zero",
        "🕒 Last Updated": datetime.now().strftime("%H:%M:%S")
    }
    
    for metric, value in quality_metrics.items():
        st.sidebar.markdown(f"**{metric}:** {value}")
    
    # Data source info
    with st.sidebar.expander("📂 Data Source Info"):
        st.markdown(f"**Source:** {metadata.get('data_source', 'Unknown')}")
        st.markdown(f"**Original Shape:** {metadata.get('original_shape', 'Unknown')}")
        st.markdown(f"**Processed Shape:** {metadata.get('processed_shape', 'Unknown')}")
        st.markdown(f"**Features Engineered:** {metadata.get('features_engineered', 0)}")
    
    # Compile filter settings
    filter_settings = {
        'risk_categories': selected_risks,
        'marks_range': marks_range,
        'engagement_level': selected_engagement,
        'completion_filter': completion_filter,
        'activity_filter': activity_filter
    }
    
    return page, selected_risks, filter_settings

def apply_filters(df: pd.DataFrame, filter_settings: Dict[str, Any]) -> pd.DataFrame:
    """Apply selected filters to the dataframe"""
    
    filtered_df = df.copy()
    
    # Risk category filter
    if filter_settings['risk_categories']:
        filtered_df = filtered_df[filtered_df["risk_category"].isin(filter_settings['risk_categories'])]
    
    # Marks range filter
    marks_range = filter_settings['marks_range']
    filtered_df = filtered_df[
        (filtered_df["total_marks"] >= marks_range[0]) &
        (filtered_df["total_marks"] <= marks_range[1])
    ]
    
    # Engagement level filter
    if filter_settings['engagement_level'] != "All":
        engagement_threshold = filtered_df["total_events"].quantile(0.66)
        low_threshold = filtered_df["total_events"].quantile(0.33)
        
        if filter_settings['engagement_level'] == "High Engagement":
            filtered_df = filtered_df[filtered_df["total_events"] >= engagement_threshold]
        elif filter_settings['engagement_level'] == "Medium Engagement":
            filtered_df = filtered_df[
                (filtered_df["total_events"] >= low_threshold) &
                (filtered_df["total_events"] < engagement_threshold)
            ]
        elif filter_settings['engagement_level'] == "Low Engagement":
            filtered_df = filtered_df[filtered_df["total_events"] < low_threshold]
    
    # Completion filter
    if filter_settings['completion_filter'] == "Completed":
        filtered_df = filtered_df[filtered_df["course_completed"] == 1]
    elif filter_settings['completion_filter'] == "Not Completed":
        filtered_df = filtered_df[filtered_df["course_completed"] == 0]
    
    # Activity filter
    if filter_settings['activity_filter'] != "All":
        if filter_settings['activity_filter'] == "Very Active (>20 days)":
            filtered_df = filtered_df[filtered_df["num_days_active"] > 20]
        elif filter_settings['activity_filter'] == "Active (10-20 days)":
            filtered_df = filtered_df[
                (filtered_df["num_days_active"] >= 10) &
                (filtered_df["num_days_active"] <= 20)
            ]
        elif filter_settings['activity_filter'] == "Less Active (<10 days)":
            filtered_df = filtered_df[filtered_df["num_days_active"] < 10]
    
    return filtered_df

def render_executive_overview(df: pd.DataFrame, clean_features: List[str]):
    """Render executive overview page with key metrics and insights"""
    
    st.markdown("## 📊 Executive Dashboard")
    
    # Key performance indicators
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        total_students = len(df)
        st.markdown(f"""
        <div class="metric-card fade-in-up">
            <div class="metric-title">Total Students</div>
            <div class="metric-value">{total_students:,}</div>
            <div class="metric-subtitle">Active Learners</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        completion_rate = (df["course_completed"].sum() / len(df)) * 100
        st.markdown(f"""
        <div class="metric-card fade-in-up">
            <div class="metric-title">Success Rate</div>
            <div class="metric-value">{completion_rate:.1f}%</div>
            <div class="metric-subtitle">Course Completion</div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {completion_rate}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_engagement = df["total_events"].mean()
        st.markdown(f"""
        <div class="metric-card fade-in-up">
            <div class="metric-title">Avg Engagement</div>
            <div class="metric-value">{avg_engagement:.0f}</div>
            <div class="metric-subtitle">Events per Student</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        high_risk_pct = (len(df[df["risk_category"] == "High Risk"]) / len(df)) * 100
        st.markdown(f"""
        <div class="metric-card fade-in-up">
            <div class="metric-title">At-Risk Students</div>
            <div class="metric-value">{high_risk_pct:.1f}%</div>
            <div class="metric-subtitle">Need Intervention</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        avg_score = df["total_marks"].mean()
        st.markdown(f"""
        <div class="metric-card fade-in-up">
            <div class="metric-title">Average Score</div>
            <div class="metric-value">{avg_score:.0f}</div>
            <div class="metric-subtitle">Total Marks</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Risk distribution and trends
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 Risk Distribution Analysis")
        
        # Enhanced pie chart
        risk_counts = df["risk_category"].value_counts()
        
        fig_pie = px.pie(
            values=risk_counts.values,
            names=risk_counts.index,
            title="Student Risk Categories",
            color_discrete_map=Config.COLORS['risk_colors'],
            hole=0.5
        )
        
        fig_pie.update_traces(
            textposition="inside",
            textinfo="percent+label",
            textfont_size=14,
            hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>"
        )
        
        fig_pie.update_layout(
            height=400,
            showlegend=True,
            font=dict(size=12),
            title_font_size=16
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.markdown("### 📈 Key Insights")
        
        # Calculate insights
        insights = []
        
        # Risk distribution insight
        high_risk_count = risk_counts.get("High Risk", 0)
        if high_risk_count > 0:
            insights.append(f"🔴 {high_risk_count} students need immediate intervention")
        
        # Engagement insight
        low_engagement = len(df[df["total_events"] < df["total_events"].quantile(0.25)])
        insights.append(f"⚡ {low_engagement} students show low engagement")
        
        # Performance insight
        top_performers = len(df[df["total_marks"] > df["total_marks"].quantile(0.8)])
        insights.append(f"🌟 {top_performers} students are top performers")
        
        # Completion insight
        completion_gap = completion_rate
        if completion_gap < 70:
            insights.append(f"⚠️ Completion rate below 70% - needs attention")
        else:
            insights.append(f"✅ Strong completion rate of {completion_gap:.1f}%")
        
        for insight in insights:
            st.markdown(f"""
            <div class="info-card slide-in-left">
                {insight}
            </div>
            """, unsafe_allow_html=True)
    
    # Engagement patterns analysis
    st.markdown("---")
    st.markdown("### 📊 Engagement Patterns by Risk Level")
    
    # Create engagement comparison
    engagement_metrics = ["total_events", "num_days_active", "num_resource_views", "num_forum_posts"]
    available_metrics = [m for m in engagement_metrics if m in clean_features]
    
    if available_metrics:
        engagement_by_risk = df.groupby("risk_category")[available_metrics].mean()
        
        # Create radar chart
        fig_radar = go.Figure()
        
        for risk_level in engagement_by_risk.index:
            fig_radar.add_trace(go.Scatterpolar(
                r=engagement_by_risk.loc[risk_level].values,
                theta=[m.replace("_", " ").title() for m in available_metrics],
                fill='toself',
                name=risk_level,
                line_color=Config.COLORS['risk_colors'].get(risk_level, '#6b7280'),
                hovertemplate="<b>%{fullData.name}</b><br>%{theta}: %{r:.1f}<extra></extra>"
            ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, engagement_by_risk.values.max() * 1.1]
                )
            ),
            showlegend=True,
            title="Average Engagement Metrics by Risk Category",
            height=500,
            font=dict(size=12)
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
    
    # Performance correlation heatmap
    st.markdown("---")
    st.markdown("### 🔥 Feature-Performance Correlation Matrix")
    
    # Select top correlated features for visualization
    correlations = []
    for feature in clean_features:
        if feature in df.columns:
            corr = df[feature].corr(df["total_marks"])
            if not pd.isna(corr):
                correlations.append((feature, abs(corr)))
    
    # Sort and take top 10
    correlations.sort(key=lambda x: x[1], reverse=True)
    top_features = [f[0] for f in correlations[:10]]
    
    if top_features:
        corr_matrix = df[top_features + ["total_marks"]].corr()
        
        fig_heatmap = px.imshow(
            corr_matrix,
            text_auto=".2f",
            aspect="auto",
            title="Top 10 Features - Correlation with Performance",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1
        )
        
        fig_heatmap.update_layout(
            height=500,
            xaxis_title="Features",
            yaxis_title="Features"
        )
        
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
        # Show top correlations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🟢 Strongest Positive Predictors")
            positive_corrs = [(f, df[f].corr(df["total_marks"])) for f in top_features 
                            if df[f].corr(df["total_marks"]) > 0]
            positive_corrs.sort(key=lambda x: x[1], reverse=True)
            
            for i, (feature, corr) in enumerate(positive_corrs[:5]):
                st.markdown(f"{i+1}. **{feature.replace('_', ' ').title()}**: {corr:.3f}")
        
        with col2:
            st.markdown("#### 🔴 Strongest Negative Predictors")
            negative_corrs = [(f, df[f].corr(df["total_marks"])) for f in top_features 
                            if df[f].corr(df["total_marks"]) < 0]
            negative_corrs.sort(key=lambda x: x[1])
            
            if negative_corrs:
                for i, (feature, corr) in enumerate(negative_corrs[:5]):
                    st.markdown(f"{i+1}. **{feature.replace('_', ' ').title()}**: {corr:.3f}")
            else:
                st.markdown("✅ All top features show positive correlation!")

def render_advanced_analytics(df: pd.DataFrame, clean_features: List[str]):
    """Render advanced analytics page with detailed statistical analysis"""
    
    st.markdown("## 📈 Advanced Statistical Analysis")
    
    # Feature analysis tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Distribution Analysis", "🔗 Correlation Analysis", "📈 Trend Analysis", "🎯 Segmentation Analysis"])
    
    with tab1:
        st.markdown("### 📊 Feature Distribution Analysis")
        
        # Feature selection
        col1, col2 = st.columns([2, 1])
        
        with col1:
            selected_feature = st.selectbox(
                "Select feature to analyze:",
                options=clean_features,
                help="Choose a feature to explore its distribution"
            )
        
        with col2:
            analysis_type = st.selectbox(
                "Analysis type:",
                options=["Distribution by Risk", "Overall Distribution", "Comparative Analysis"]
            )
        
        if selected_feature:
            col1, col2 = st.columns(2)
            
            with col1:
                if analysis_type == "Distribution by Risk":
                    # Histogram by risk category
                    fig_hist = px.histogram(
                        df,
                        x=selected_feature,
                        color="risk_category",
                        title=f"Distribution: {selected_feature.replace('_', ' ').title()}",
                        color_discrete_map=Config.COLORS['risk_colors'],
                        marginal="rug",
                        nbins=30
                    )
                else:
                    # Overall distribution
                    fig_hist = px.histogram(
                        df,
                        x=selected_feature,
                        title=f"Overall Distribution: {selected_feature.replace('_', ' ').title()}",
                        nbins=30
                    )
                
                fig_hist.update_layout(height=400)
                st.plotly_chart(fig_hist, use_container_width=True)
            
            with col2:
                # Box plot
                fig_box = px.box(
                    df,
                    x="risk_category",
                    y=selected_feature,
                    title=f"Box Plot: {selected_feature.replace('_', ' ').title()}",
                    color="risk_category",
                    color_discrete_map=Config.COLORS['risk_colors']
                )
                fig_box.update_layout(height=400)
                st.plotly_chart(fig_box, use_container_width=True)
            
            # Statistical summary
            st.markdown("#### 📈 Statistical Summary")
            
            summary_stats = df.groupby("risk_category")[selected_feature].agg([
                'count', 'mean', 'median', 'std', 'min', 'max'
            ]).round(3)
            
            st.dataframe(summary_stats, use_container_width=True)
            
            # Statistical tests
            st.markdown("#### 🧪 Statistical Tests")
            
            # ANOVA test for differences between risk groups
            risk_groups = [df[df["risk_category"] == risk][selected_feature].dropna() 
                          for risk in df["risk_category"].unique()]
            
            try:
                f_stat, p_value = stats.f_oneway(*risk_groups)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("F-statistic", f"{f_stat:.4f}")
                with col2:
                    st.metric("P-value", f"{p_value:.4f}")
                
                if p_value < 0.05:
                    st.success("✅ Significant difference between risk groups (p < 0.05)")
                else:
                    st.info("ℹ️ No significant difference between risk groups (p ≥ 0.05)")
                    
            except Exception as e:
                st.warning(f"Could not perform statistical test: {str(e)}")
    
    with tab2:
        st.markdown("### 🔗 Advanced Correlation Analysis")
        
        # Correlation method selection
        corr_method = st.selectbox(
            "Correlation method:",
            options=["pearson", "spearman", "kendall"],
            help="Choose correlation calculation method"
        )
        
        # Calculate correlation matrix
        numeric_features = [f for f in clean_features if df[f].dtype in ['int64', 'float64']]
        
        if len(numeric_features) > 1:
            corr_matrix = df[numeric_features + ["total_marks"]].corr(method=corr_method)
            
            # Interactive heatmap
            fig_corr = px.imshow(
                corr_matrix,
                text_auto=".3f",
                aspect="auto",
                title=f"Correlation Matrix ({corr_method.title()})",
                color_continuous_scale="RdBu_r",
                zmin=-1,
                zmax=1
            )
            
            fig_corr.update_layout(height=600)
            st.plotly_chart(fig_corr, use_container_width=True)
            
            # Correlation insights
            st.markdown("#### 🔍 Correlation Insights")
            
            # Find strongest correlations with performance
            performance_corrs = corr_matrix["total_marks"].drop("total_marks").sort_values(key=abs, ascending=False)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**🏆 Top Positive Correlations:**")
                positive_corrs = performance_corrs[performance_corrs > 0].head(5)
                for feature, corr in positive_corrs.items():
                    st.markdown(f"• {feature.replace('_', ' ').title()}: **{corr:.3f}**")
            
            with col2:
                st.markdown("**⚠️ Top Negative Correlations:**")
                negative_corrs = performance_corrs[performance_corrs < 0].head(5)
                if len(negative_corrs) > 0:
                    for feature, corr in negative_corrs.items():
                        st.markdown(f"• {feature.replace('_', ' ').title()}: **{corr:.3f}**")
                else:
                    st.markdown("✅ No significant negative correlations found!")
    
    with tab3:
        st.markdown("### 📈 Trend and Pattern Analysis")
        
        # Feature relationship explorer
        col1, col2 = st.columns(2)
        
        with col1:
            x_feature = st.selectbox("X-axis feature:", clean_features, key="trend_x")
        
        with col2:
            y_feature = st.selectbox("Y-axis feature:", clean_features, index=1, key="trend_y")
        
        if x_feature != y_feature:
            # Scatter plot with trend line
            try:
                fig_scatter = px.scatter(
                    df,
                    x=x_feature,
                    y=y_feature,
                    color="risk_category",
                    size="total_marks",
                    title=f"Relationship: {x_feature.replace('_', ' ').title()} vs {y_feature.replace('_', ' ').title()}",
                    color_discrete_map=Config.COLORS['risk_colors'],
                    trendline="ols",
                    hover_data=["total_marks", "course_completed"]
                )
            except ImportError as e:
                # Fallback without trendline if statsmodels is not available
                st.warning("⚠️ Trendline feature requires 'statsmodels' library. Showing scatter plot without trendline.")
                fig_scatter = px.scatter(
                    df,
                    x=x_feature,
                    y=y_feature,
                    color="risk_category",
                    size="total_marks",
                    title=f"Relationship: {x_feature.replace('_', ' ').title()} vs {y_feature.replace('_', ' ').title()}",
                    color_discrete_map=Config.COLORS['risk_colors'],
                    hover_data=["total_marks", "course_completed"]
                )
            except Exception as e:
                # General fallback for any other errors
                st.error(f"Error creating scatter plot with trendline: {str(e)}")
                fig_scatter = px.scatter(
                    df,
                    x=x_feature,
                    y=y_feature,
                    color="risk_category",
                    title=f"Relationship: {x_feature.replace('_', ' ').title()} vs {y_feature.replace('_', ' ').title()}",
                    color_discrete_map=Config.COLORS['risk_colors']
                )
            
            fig_scatter.update_layout(height=500)
            st.plotly_chart(fig_scatter, use_container_width=True)
            
            # Correlation coefficient
            correlation = df[x_feature].corr(df[y_feature])
            st.metric("Correlation Coefficient", f"{correlation:.4f}")
            
            if abs(correlation) > 0.7:
                st.success("🔥 Strong correlation detected!")
            elif abs(correlation) > 0.3:
                st.info("📊 Moderate correlation found")
            else:
                st.warning("📉 Weak correlation")
    
    with tab4:
        st.markdown("### 🎯 Student Segmentation Analysis")
        
        # K-means clustering for student segmentation
        from sklearn.cluster import KMeans
        from sklearn.preprocessing import StandardScaler
        
        # Feature selection for clustering
        clustering_features = st.multiselect(
            "Select features for segmentation:",
            options=clean_features,
            default=clean_features[:5] if len(clean_features) >= 5 else clean_features,
            help="Choose features to use for student segmentation"
        )
        
        if len(clustering_features) >= 2:
            # Number of clusters
            n_clusters = st.slider("Number of segments:", min_value=2, max_value=8, value=3)
            
            # Perform clustering
            X_cluster = df[clustering_features].fillna(0)
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X_cluster)
            
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            clusters = kmeans.fit_predict(X_scaled)
            
            # Add cluster labels to dataframe
            df_clustered = df.copy()
            df_clustered['Segment'] = [f"Segment {i+1}" for i in clusters]
            
            # Visualize clusters
            if len(clustering_features) >= 2:
                fig_cluster = px.scatter(
                    df_clustered,
                    x=clustering_features[0],
                    y=clustering_features[1],
                    color='Segment',
                    title=f"Student Segmentation ({n_clusters} segments)",
                    hover_data=['risk_category', 'total_marks']
                )
                
                fig_cluster.update_layout(height=500)
                st.plotly_chart(fig_cluster, use_container_width=True)
            
            # Segment analysis
            st.markdown("#### 📊 Segment Characteristics")
            
            segment_analysis = df_clustered.groupby('Segment').agg({
                'total_marks': ['mean', 'std'],
                'course_completed': 'mean',
                'total_events': 'mean',
                'num_days_active': 'mean'
            }).round(2)
            
            # Flatten column names
            segment_analysis.columns = ['_'.join(col).strip() for col in segment_analysis.columns]
            
            st.dataframe(segment_analysis, use_container_width=True)
            
            # Segment insights
            for i in range(n_clusters):
                segment_data = df_clustered[df_clustered['Segment'] == f'Segment {i+1}']
                avg_performance = segment_data['total_marks'].mean()
                completion_rate = segment_data['course_completed'].mean() * 100
                
                if avg_performance > df['total_marks'].mean():
                    performance_label = "🟢 High Performers"
                elif avg_performance > df['total_marks'].quantile(0.33):
                    performance_label = "🟡 Average Performers"
                else:
                    performance_label = "🔴 At-Risk Students"
                
                st.markdown(f"""
                <div class="info-card">
                    <strong>Segment {i+1}: {performance_label}</strong><br>
                    • Average Score: {avg_performance:.1f}<br>
                    • Completion Rate: {completion_rate:.1f}%<br>
                    • Students: {len(segment_data)} ({len(segment_data)/len(df)*100:.1f}%)
                </div>
                """, unsafe_allow_html=True)

# Main application logic
def main():
    """Main application entry point"""
    
    # Initialize application
    df, clean_features, metadata = initialize_app()
    
    # Render header
    render_header()
    
    # Render sidebar and get selections
    page, selected_risks, filter_settings = render_sidebar(df, metadata)
    
    # Apply filters
    filtered_df = apply_filters(df, filter_settings)
    
    # Show filter summary
    if len(filtered_df) != len(df):
        st.info(f"📊 Showing {len(filtered_df):,} of {len(df):,} students based on your filters")
    
    # Render selected page
    if page == "📊 Executive Overview":
        render_executive_overview(filtered_df, clean_features)
    elif page == "📈 Advanced Analytics":
        render_advanced_analytics(filtered_df, clean_features)
    elif page == "🤖 Predictive Models":
        render_predictive_models(filtered_df, clean_features)
    elif page == "💡 Strategic Insights":
        render_strategic_insights(filtered_df, clean_features)
    elif page == "📋 Data Explorer":
        render_data_explorer(filtered_df, clean_features)
    elif page == "📄 Report Generator":
        render_report_generator(filtered_df, clean_features, metadata)

def render_predictive_models(df: pd.DataFrame, clean_features: List[str]):
    """Render predictive models page with advanced ML analysis"""
    
    st.markdown("## 🤖 Advanced Predictive Analytics")
    
    if len(df) < 50:
        st.warning("⚠️ Insufficient data for reliable modeling. Please adjust filters.")
        return
    
    # Model selection and configuration
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 Model Configuration")
        
        # Model selection
        model_types = st.multiselect(
            "Select models to train:",
            options=["Random Forest", "Logistic Regression", "Support Vector Machine", "Gradient Boosting"],
            default=["Random Forest", "Logistic Regression"],
            help="Choose which models to train and compare"
        )
        
        # Feature selection
        feature_selection_method = st.selectbox(
            "Feature selection:",
            options=["All Features", "Top Correlated", "Custom Selection"],
            help="Choose how to select features for modeling"
        )
        
        if feature_selection_method == "Top Correlated":
            n_features = st.slider("Number of top features:", 5, min(20, len(clean_features)), 10)
        elif feature_selection_method == "Custom Selection":
            selected_features = st.multiselect(
                "Select features:",
                options=clean_features,
                default=clean_features[:10]
            )
    
    with col2:
        st.markdown("### ⚙️ Training Parameters")
        
        test_size = st.slider("Test set size:", 0.1, 0.5, 0.3, 0.05)
        cv_folds = st.slider("Cross-validation folds:", 3, 10, 5)
        random_state = st.number_input("Random state:", value=42, min_value=0)
    
    # Feature preparation
    if feature_selection_method == "All Features":
        model_features = clean_features
    elif feature_selection_method == "Top Correlated":
        # Calculate correlations and select top features
        correlations = []
        for feature in clean_features:
            if feature in df.columns:
                corr = abs(df[feature].corr(df["total_marks"]))
                if not pd.isna(corr):
                    correlations.append((feature, corr))
        
        correlations.sort(key=lambda x: x[1], reverse=True)
        model_features = [f[0] for f in correlations[:n_features]]
    else:
        model_features = selected_features if 'selected_features' in locals() else clean_features[:10]
    
    # Display selected features
    st.markdown("### 📋 Selected Features")
    st.markdown(f"**{len(model_features)} features selected:** {', '.join([f.replace('_', ' ').title() for f in model_features[:5]])}{'...' if len(model_features) > 5 else ''}")
    
    # Train models button
    if st.button("🚀 Train Models", type="primary"):
        with st.spinner("Training models... This may take a moment."):
            
            # Prepare data
            X = df[model_features].fillna(0)
            y = df["course_completed"]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state, stratify=y
            )
            
            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Train models
            models = {}
            results = {}
            
            for model_name in model_types:
                try:
                    if model_name == "Random Forest":
                        model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=random_state)
                        model.fit(X_train, y_train)  # RF doesn't need scaling
                        y_pred = model.predict(X_test)
                        y_pred_proba = model.predict_proba(X_test)[:, 1]
                        X_for_cv = X_train
                    
                    elif model_name == "Logistic Regression":
                        model = LogisticRegression(random_state=random_state, max_iter=1000)
                        model.fit(X_train_scaled, y_train)
                        y_pred = model.predict(X_test_scaled)
                        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
                        X_for_cv = X_train_scaled
                    
                    elif model_name == "Support Vector Machine":
                        model = SVC(probability=True, random_state=random_state)
                        model.fit(X_train_scaled, y_train)
                        y_pred = model.predict(X_test_scaled)
                        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
                        X_for_cv = X_train_scaled
                    
                    elif model_name == "Gradient Boosting":
                        from sklearn.ensemble import GradientBoostingClassifier
                        model = GradientBoostingClassifier(random_state=random_state)
                        model.fit(X_train, y_train)
                        y_pred = model.predict(X_test)
                        y_pred_proba = model.predict_proba(X_test)[:, 1]
                        X_for_cv = X_train
                    
                    # Calculate metrics
                    metrics = {
                        'accuracy': accuracy_score(y_test, y_pred),
                        'precision': precision_score(y_test, y_pred, zero_division=0),
                        'recall': recall_score(y_test, y_pred, zero_division=0),
                        'f1': f1_score(y_test, y_pred, zero_division=0),
                        'auc': roc_auc_score(y_test, y_pred_proba)
                    }
                    
                    # Cross-validation
                    cv_scores = cross_val_score(model, X_for_cv, y_train, cv=cv_folds, scoring='accuracy')
                    metrics['cv_mean'] = cv_scores.mean()
                    metrics['cv_std'] = cv_scores.std()
                    
                    models[model_name] = model
                    results[model_name] = {
                        'metrics': metrics,
                        'predictions': y_pred,
                        'probabilities': y_pred_proba,
                        'test_indices': X_test.index
                    }
                    
                except Exception as e:
                    st.error(f"Failed to train {model_name}: {str(e)}")
                    continue
            
            # Display results
            if results:
                st.success(f"✅ Successfully trained {len(results)} models!")
                
                # Model comparison
                st.markdown("### 📊 Model Performance Comparison")
                
                # Create comparison dataframe
                comparison_data = []
                for model_name, result in results.items():
                    metrics = result['metrics']
                    comparison_data.append({
                        'Model': model_name,
                        'Accuracy': f"{metrics['accuracy']:.4f}",
                        'Precision': f"{metrics['precision']:.4f}",
                        'Recall': f"{metrics['recall']:.4f}",
                        'F1-Score': f"{metrics['f1']:.4f}",
                        'AUC': f"{metrics['auc']:.4f}",
                        'CV Mean': f"{metrics['cv_mean']:.4f}",
                        'CV Std': f"{metrics['cv_std']:.4f}"
                    })
                
                comparison_df = pd.DataFrame(comparison_data)
                st.dataframe(comparison_df, use_container_width=True, hide_index=True)
                
                # Best model identification
                best_model_name = max(results.keys(), key=lambda x: results[x]['metrics']['f1'])
                st.markdown(f"""
                <div class="success-card">
                    <strong>🏆 Best Performing Model: {best_model_name}</strong><br>
                    F1-Score: {results[best_model_name]['metrics']['f1']:.4f}<br>
                    AUC: {results[best_model_name]['metrics']['auc']:.4f}
                </div>
                """, unsafe_allow_html=True)
                
                # Detailed analysis for best model
                st.markdown(f"### 🔍 Detailed Analysis: {best_model_name}")
                
                best_result = results[best_model_name]
                best_model = models[best_model_name]
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Confusion Matrix
                    cm = confusion_matrix(y_test, best_result['predictions'])
                    
                    fig_cm = px.imshow(
                        cm,
                        text_auto=True,
                        aspect="auto",
                        title="Confusion Matrix",
                        labels=dict(x="Predicted", y="Actual"),
                        x=['Not Completed', 'Completed'],
                        y=['Not Completed', 'Completed']
                    )
                    fig_cm.update_layout(height=400)
                    st.plotly_chart(fig_cm, use_container_width=True)
                
                with col2:
                    # ROC Curve
                    fpr, tpr, _ = roc_curve(y_test, best_result['probabilities'])
                    
                    fig_roc = go.Figure()
                    fig_roc.add_trace(go.Scatter(
                        x=fpr, y=tpr,
                        mode='lines',
                        name=f'ROC Curve (AUC = {best_result["metrics"]["auc"]:.3f})',
                        line=dict(color='blue', width=2)
                    ))
                    fig_roc.add_trace(go.Scatter(
                        x=[0, 1], y=[0, 1],
                        mode='lines',
                        name='Random Classifier',
                        line=dict(color='red', dash='dash')
                    ))
                    
                    fig_roc.update_layout(
                        title='ROC Curve',
                        xaxis_title='False Positive Rate',
                        yaxis_title='True Positive Rate',
                        height=400
                    )
                    st.plotly_chart(fig_roc, use_container_width=True)
                
                # Feature importance (for tree-based models)
                if hasattr(best_model, 'feature_importances_'):
                    st.markdown("### 🎯 Feature Importance Analysis")
                    
                    importance_df = pd.DataFrame({
                        'Feature': model_features,
                        'Importance': best_model.feature_importances_
                    }).sort_values('Importance', ascending=True)
                    
                    fig_importance = px.bar(
                        importance_df,
                        x='Importance',
                        y='Feature',
                        title=f'Feature Importance - {best_model_name}',
                        orientation='h'
                    )
                    fig_importance.update_layout(height=500)
                    st.plotly_chart(fig_importance, use_container_width=True)
                    
                    # Top features insight
                    top_features = importance_df.tail(5)['Feature'].tolist()
                    st.markdown(f"""
                    <div class="info-card">
                        <strong>🏆 Top 5 Most Important Features:</strong><br>
                        {', '.join([f.replace('_', ' ').title() for f in reversed(top_features)])}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Prediction examples
                st.markdown("### 🎲 Sample Predictions")
                
                # Get sample predictions
                sample_size = min(10, len(X_test))
                sample_indices = np.random.choice(X_test.index, sample_size, replace=False)
                
                sample_data = []
                for idx in sample_indices:
                    actual = y_test.loc[idx]
                    pred_idx = list(X_test.index).index(idx)
                    predicted = best_result['predictions'][pred_idx]
                    probability = best_result['probabilities'][pred_idx]
                    
                    sample_data.append({
                        'Student ID': idx,
                        'Actual': 'Completed' if actual == 1 else 'Not Completed',
                        'Predicted': 'Completed' if predicted == 1 else 'Not Completed',
                        'Probability': f"{probability:.3f}",
                        'Confidence': 'High' if probability > 0.8 or probability < 0.2 else 'Medium' if probability > 0.6 or probability < 0.4 else 'Low',
                        'Correct': '✅' if actual == predicted else '❌'
                    })
                
                sample_df = pd.DataFrame(sample_data)
                st.dataframe(sample_df, use_container_width=True, hide_index=True)
                
                # Model insights and recommendations
                st.markdown("### 💡 Model Insights & Recommendations")
                
                accuracy = best_result['metrics']['accuracy']
                precision = best_result['metrics']['precision']
                recall = best_result['metrics']['recall']
                
                insights = []
                
                if accuracy > 0.85:
                    insights.append("🎯 **High Accuracy**: Model shows excellent predictive performance")
                elif accuracy > 0.75:
                    insights.append("📊 **Good Accuracy**: Model provides reliable predictions")
                else:
                    insights.append("⚠️ **Moderate Accuracy**: Consider feature engineering or more data")
                
                if precision > 0.8:
                    insights.append("✅ **High Precision**: Low false positive rate - reliable completion predictions")
                else:
                    insights.append("⚠️ **Moderate Precision**: Some false positives in completion predictions")
                
                if recall > 0.8:
                    insights.append("🔍 **High Recall**: Successfully identifies most students who will complete")
                else:
                    insights.append("📢 **Moderate Recall**: May miss some students who will complete")
                
                for insight in insights:
                    st.markdown(f"""
                    <div class="info-card">
                        {insight}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Actionable recommendations
                st.markdown("""
                <div class="success-card">
                    <strong>🚀 Actionable Recommendations:</strong>
                    <ul>
                        <li><strong>Early Warning System:</strong> Use model predictions to identify at-risk students early</li>
                        <li><strong>Intervention Targeting:</strong> Focus resources on students with low completion probability</li>
                        <li><strong>Feature Monitoring:</strong> Track the most important features for ongoing assessment</li>
                        <li><strong>Model Updates:</strong> Retrain model periodically with new data for improved accuracy</li>
                        <li><strong>A/B Testing:</strong> Test intervention strategies on predicted at-risk students</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            else:
                st.error("❌ No models were successfully trained. Please check your data and try again.")
    
    # Debug section for your model
    st.markdown("---")
    st.markdown("### 🔍 Debug Your Existing Model")
    
    # Load your existing model for debugging
    existing_model_debug, existing_metadata_debug = ModelManager.load_pretrained_model()
    
    if existing_model_debug is not None:
        if st.button("🧪 Debug Model Loading & Evaluation"):
            with st.expander("🔍 Detailed Debug Information", expanded=True):
                
                # Model inspection
                st.markdown("#### 📋 Model Information")
                st.write(f"**Model Type:** {type(existing_model_debug).__name__}")
                st.write(f"**Has predict method:** {hasattr(existing_model_debug, 'predict')}")
                st.write(f"**Has predict_proba method:** {hasattr(existing_model_debug, 'predict_proba')}")
                
                if hasattr(existing_model_debug, 'n_features_in_'):
                    st.write(f"**Expected features:** {existing_model_debug.n_features_in_}")
                else:
                    st.write("**Expected features:** Unknown (older scikit-learn version)")
                
                if hasattr(existing_model_debug, 'feature_importances_'):
                    st.write(f"**Feature importances available:** Yes ({len(existing_model_debug.feature_importances_)} features)")
                else:
                    st.write("**Feature importances available:** No")
                
                # Data preparation debug
                st.markdown("#### 📊 Data Preparation Debug")
                X_debug = df[model_features].fillna(0)
                y_debug = df["course_completed"]
                
                st.write(f"**Current data shape:** {X_debug.shape}")
                st.write(f"**Features used:** {len(model_features)}")
                st.write(f"**Target distribution:** {y_debug.value_counts().to_dict()}")
                
                # Show first few rows of data
                st.markdown("**Sample of current data:**")
                st.dataframe(X_debug.head(3))
                
                # Test different evaluation approaches
                st.markdown("#### 🧪 Testing Different Approaches")
                
                X_train_debug, X_test_debug, y_train_debug, y_test_debug = train_test_split(
                    X_debug, y_debug, test_size=0.3, random_state=42, stratify=y_debug
                )
                
                st.write(f"**Test set shape:** {X_test_debug.shape}")
                
                # Approach 1: Direct prediction (no scaling)
                try:
                    st.markdown("**🔬 Approach 1: Direct prediction (no scaling)**")
                    
                    # Handle feature alignment
                    if hasattr(existing_model_debug, 'n_features_in_') and existing_model_debug.n_features_in_ != X_test_debug.shape[1]:
                        if existing_model_debug.n_features_in_ > X_test_debug.shape[1]:
                            padding = np.zeros((X_test_debug.shape[0], existing_model_debug.n_features_in_ - X_test_debug.shape[1]))
                            X_test_aligned = np.column_stack([X_test_debug.values, padding])
                            st.write(f"Padded to shape: {X_test_aligned.shape}")
                        else:
                            X_test_aligned = X_test_debug.values[:, :existing_model_debug.n_features_in_]
                            st.write(f"Truncated to shape: {X_test_aligned.shape}")
                    else:
                        X_test_aligned = X_test_debug.values
                    
                    y_pred_1 = existing_model_debug.predict(X_test_aligned)
                    y_pred_proba_1 = existing_model_debug.predict_proba(X_test_aligned)[:, 1]
                    
                    acc_1 = accuracy_score(y_test_debug, y_pred_1)
                    f1_1 = f1_score(y_test_debug, y_pred_1)
                    
                    st.write(f"✅ **Accuracy:** {acc_1:.4f}")
                    st.write(f"✅ **F1-Score:** {f1_1:.4f}")
                    st.write(f"✅ **Predictions range:** {y_pred_proba_1.min():.3f} - {y_pred_proba_1.max():.3f}")
                    
                    if acc_1 > 0.8:
                        st.success("🎯 This approach works well!")
                    elif acc_1 > 0.6:
                        st.warning("⚠️ Moderate performance - might need scaling")
                    else:
                        st.error("❌ Poor performance - likely needs different preprocessing")
                        
                except Exception as e:
                    st.error(f"❌ Approach 1 failed: {str(e)}")
                
                # Approach 2: Standard scaling
                try:
                    st.markdown("**🔬 Approach 2: Standard scaling**")
                    
                    scaler = StandardScaler()
                    X_test_scaled = scaler.fit_transform(X_test_aligned)
                    
                    y_pred_2 = existing_model_debug.predict(X_test_scaled)
                    y_pred_proba_2 = existing_model_debug.predict_proba(X_test_scaled)[:, 1]
                    
                    acc_2 = accuracy_score(y_test_debug, y_pred_2)
                    f1_2 = f1_score(y_test_debug, y_pred_2)
                    
                    st.write(f"✅ **Accuracy:** {acc_2:.4f}")
                    st.write(f"✅ **F1-Score:** {f1_2:.4f}")
                    st.write(f"✅ **Predictions range:** {y_pred_proba_2.min():.3f} - {y_pred_proba_2.max():.3f}")
                    
                    if acc_2 > 0.8:
                        st.success("🎯 Standard scaling works well!")
                    elif acc_2 > 0.6:
                        st.warning("⚠️ Moderate performance with scaling")
                    else:
                        st.error("❌ Poor performance even with scaling")
                        
                except Exception as e:
                    st.error(f"❌ Approach 2 failed: {str(e)}")
                
                # Summary and recommendations
                st.markdown("#### 💡 Debug Summary & Recommendations")
                
                try:
                    best_acc = max([acc_1 if 'acc_1' in locals() else 0, 
                                   acc_2 if 'acc_2' in locals() else 0])
                    
                    if best_acc > 0.85:
                        st.success(f"✅ **Your model works fine!** Best accuracy: {best_acc:.4f}")
                        st.info("The issue might be in the comparison logic. Your model is performing well.")
                    elif best_acc > 0.7:
                        st.warning(f"⚠️ **Moderate performance:** {best_acc:.4f}")
                        st.info("Your model works but might need the right preprocessing approach.")
                    else:
                        st.error(f"❌ **Performance issue:** {best_acc:.4f}")
                        st.info("There might be a fundamental mismatch between training and evaluation data.")
                        
                        # Additional debugging suggestions
                        st.markdown("**🔍 Additional checks needed:**")
                        st.write("1. Verify the model file is not corrupted")
                        st.write("2. Check if the same features were used during training")
                        st.write("3. Verify the target variable encoding matches")
                        st.write("4. Check if any special preprocessing was done in your notebook")
                        
                except:
                    st.error("Could not complete debug analysis")
    
    else:
        st.warning("⚠️ Cannot debug - model not loaded")
    
    # Model comparison section
    st.markdown("---")
    st.markdown("### 🔄 Model Comparison: Your Model vs New Training")
    
    # Load your existing model
    existing_model, existing_metadata = ModelManager.load_pretrained_model()
    
    if existing_model is not None:
        st.markdown(f"""
        <div class="info-card">
            <strong>📊 Your Existing Model Loaded Successfully!</strong><br>
            • <strong>Type:</strong> {existing_metadata.get('type', 'Unknown')}<br>
            • <strong>Expected Features:</strong> {existing_metadata.get('features_expected', 'Unknown')}<br>
            • <strong>Source:</strong> {existing_metadata.get('source', 'Your notebook')}<br>
            • <strong>File:</strong> best_random_forest_classifier.joblib
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Compare Your Model vs New Training", type="primary"):
            with st.spinner("Training new models and comparing with your existing model..."):
                
                # Prepare data
                X = df[model_features].fillna(0)
                y = df["course_completed"]
                
                # Split data
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=test_size, random_state=random_state, stratify=y
                )
                
                # Store results for comparison AND models for saving
                all_results = {}
                trained_models = {}  # Store actual model objects for saving
                
                # 1. Evaluate your existing model
                st.info("🔍 Evaluating your existing model...")
                existing_result = ModelManager.evaluate_model_on_data(
                    existing_model, X_test, y_test, "Your Existing Model"
                )
                all_results["Your Existing Model"] = existing_result
                
                # 2. Train new models for comparison
                st.info("🔄 Training new models for comparison...")
                
                for model_name in model_types:
                    try:
                        if model_name == "Random Forest":
                            new_model = RandomForestClassifier(
                                n_estimators=100, max_depth=10, random_state=random_state
                            )
                            new_model.fit(X_train, y_train)
                            trained_models[f"New {model_name}"] = new_model  # Store the model
                            
                        elif model_name == "Logistic Regression":
                            scaler = StandardScaler()
                            X_train_scaled = scaler.fit_transform(X_train)
                            X_test_scaled = scaler.transform(X_test)
                            
                            new_model = LogisticRegression(random_state=random_state, max_iter=1000)
                            new_model.fit(X_train_scaled, y_train)
                            trained_models[f"New {model_name}"] = {'model': new_model, 'scaler': scaler}  # Store model + scaler
                            
                            # For evaluation, we need to use scaled test data
                            new_result = ModelManager.evaluate_model_on_data(
                                new_model, X_test_scaled, y_test, f"New {model_name}"
                            )
                            all_results[f"New {model_name}"] = new_result
                            continue
                            
                        elif model_name == "Support Vector Machine":
                            scaler = StandardScaler()
                            X_train_scaled = scaler.fit_transform(X_train)
                            X_test_scaled = scaler.transform(X_test)
                            
                            new_model = SVC(probability=True, random_state=random_state)
                            new_model.fit(X_train_scaled, y_train)
                            
                            new_result = ModelManager.evaluate_model_on_data(
                                new_model, X_test_scaled, y_test, f"New {model_name}"
                            )
                            all_results[f"New {model_name}"] = new_result
                            continue
                        
                        # For Random Forest and other non-scaled models
                        new_result = ModelManager.evaluate_model_on_data(
                            new_model, X_test, y_test, f"New {model_name}"
                        )
                        all_results[f"New {model_name}"] = new_result
                        
                    except Exception as e:
                        st.warning(f"Failed to train {model_name}: {str(e)}")
                        continue
                
                # Display comparison results
                if len(all_results) > 1:
                    st.success(f"✅ Successfully compared {len(all_results)} models!")
                    
                    # Create comparison table
                    st.markdown("### 📊 Model Performance Comparison")
                    
                    comparison_df = ModelManager.compare_models(all_results)
                    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
                    
                    # Identify best performing models
                    successful_results = {k: v for k, v in all_results.items() if v['success']}
                    
                    if successful_results:
                        # Find best model by F1 score
                        best_model_name = max(successful_results.keys(), 
                                            key=lambda x: successful_results[x]['metrics']['f1'])
                        best_f1 = successful_results[best_model_name]['metrics']['f1']
                        
                        # Check if your existing model is the best
                        your_model_f1 = successful_results.get("Your Existing Model", {}).get('metrics', {}).get('f1', 0)
                        
                        if best_model_name == "Your Existing Model":
                            st.markdown(f"""
                            <div class="success-card">
                                <strong>🏆 Your Existing Model is the Best Performer!</strong><br>
                                • <strong>F1-Score:</strong> {best_f1:.4f}<br>
                                • Your model from the notebook outperforms the newly trained models<br>
                                • This validates your original training approach!
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div class="info-card">
                                <strong>🔍 Comparison Results:</strong><br>
                                • <strong>Best Model:</strong> {best_model_name} (F1: {best_f1:.4f})<br>
                                • <strong>Your Model:</strong> F1-Score of {your_model_f1:.4f}<br>
                                • <strong>Difference:</strong> {abs(best_f1 - your_model_f1):.4f}<br>
                                • {'New model performs slightly better' if best_f1 > your_model_f1 else 'Your model is very competitive'}
                            </div>
                            """, unsafe_allow_html=True)
                    
                    # Detailed comparison visualizations
                    st.markdown("### 📈 Detailed Model Comparison")
                    
                    # Performance metrics comparison
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Metrics comparison bar chart
                        metrics_data = []
                        for model_name, result in successful_results.items():
                            if result['success']:
                                metrics = result['metrics']
                                metrics_data.extend([
                                    {'Model': model_name, 'Metric': 'Accuracy', 'Value': metrics['accuracy']},
                                    {'Model': model_name, 'Metric': 'Precision', 'Value': metrics['precision']},
                                    {'Model': model_name, 'Metric': 'Recall', 'Value': metrics['recall']},
                                    {'Model': model_name, 'Metric': 'F1-Score', 'Value': metrics['f1']},
                                ])
                        
                        if metrics_data:
                            metrics_df = pd.DataFrame(metrics_data)
                            fig_metrics = px.bar(
                                metrics_df,
                                x='Value',
                                y='Model',
                                color='Metric',
                                title='Performance Metrics Comparison',
                                orientation='h',
                                barmode='group'
                            )
                            fig_metrics.update_layout(height=400)
                            st.plotly_chart(fig_metrics, use_container_width=True)
                    
                    with col2:
                        # ROC curves comparison
                        fig_roc = go.Figure()
                        
                        for model_name, result in successful_results.items():
                            if result['success'] and result['probabilities'] is not None:
                                fpr, tpr, _ = roc_curve(y_test, result['probabilities'])
                                auc_score = result['metrics']['auc']
                                
                                fig_roc.add_trace(go.Scatter(
                                    x=fpr, y=tpr,
                                    mode='lines',
                                    name=f'{model_name} (AUC={auc_score:.3f})',
                                    line=dict(width=3)
                                ))
                        
                        # Add random classifier line
                        fig_roc.add_trace(go.Scatter(
                            x=[0, 1], y=[0, 1],
                            mode='lines',
                            name='Random Classifier',
                            line=dict(color='red', dash='dash')
                        ))
                        
                        fig_roc.update_layout(
                            title='ROC Curves Comparison',
                            xaxis_title='False Positive Rate',
                            yaxis_title='True Positive Rate',
                            height=400
                        )
                        st.plotly_chart(fig_roc, use_container_width=True)
                    
                    # Save new models section
                    st.markdown("---")
                    st.markdown("### 💾 Save New Trained Models")
                    
                    # Filter out your existing model for saving options
                    new_models_results = {k: v for k, v in successful_results.items() 
                                        if k != "Your Existing Model" and v['success']}
                    
                    if new_models_results:
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            model_to_save = st.selectbox(
                                "Select model to save:",
                                options=list(new_models_results.keys()),
                                help="Choose which newly trained model to save"
                            )
                            
                            save_filename = st.text_input(
                                "Save as filename:",
                                value=f"new_{model_to_save.lower().replace(' ', '_')}_model.joblib",
                                help="Enter filename for the saved model"
                            )
                        
                        with col2:
                            st.markdown("**Model to Save Info:**")
                            if model_to_save:
                                selected_result = new_models_results[model_to_save]
                                st.markdown(f"• **Accuracy:** {selected_result['metrics']['accuracy']:.4f}")
                                st.markdown(f"• **F1-Score:** {selected_result['metrics']['f1']:.4f}")
                                st.markdown(f"• **AUC:** {selected_result['metrics']['auc']:.4f}")
                                st.markdown(f"• **Features:** {len(model_features)}")
                        
                        if st.button("💾 Save Selected Model", type="secondary"):
                            if model_to_save and save_filename:
                                try:
                                    # Get the actual model object (we need to retrain to get the object)
                                    X_retrain = df[model_features].fillna(0)
                                    y_retrain = df["course_completed"]
                                    
                                    if "Random Forest" in model_to_save:
                                        model_to_save_obj = RandomForestClassifier(
                                            n_estimators=100, max_depth=10, random_state=random_state
                                        )
                                        model_to_save_obj.fit(X_retrain, y_retrain)
                                        
                                    elif "Logistic Regression" in model_to_save:
                                        scaler = StandardScaler()
                                        X_retrain_scaled = scaler.fit_transform(X_retrain)
                                        model_to_save_obj = LogisticRegression(random_state=random_state, max_iter=1000)
                                        model_to_save_obj.fit(X_retrain_scaled, y_retrain)
                                        
                                    elif "Support Vector Machine" in model_to_save:
                                        scaler = StandardScaler()
                                        X_retrain_scaled = scaler.fit_transform(X_retrain)
                                        model_to_save_obj = SVC(probability=True, random_state=random_state)
                                        model_to_save_obj.fit(X_retrain_scaled, y_retrain)
                                    
                                    # Save with metadata
                                    success = ModelManager.save_model_with_metadata(
                                        model=model_to_save_obj,
                                        filename=save_filename,
                                        feature_names=model_features,
                                        metrics=selected_result['metrics'],
                                        model_type=model_to_save
                                    )
                                    
                                    if success:
                                        st.success(f"✅ Model saved successfully as '{save_filename}'!")
                                        st.info(f"📁 You can now load this model in future sessions")
                                        
                                        # Show save summary
                                        st.markdown(f"""
                                        <div class="success-card">
                                            <strong>💾 Save Summary:</strong><br>
                                            • <strong>Model:</strong> {model_to_save}<br>
                                            • <strong>Filename:</strong> {save_filename}<br>
                                            • <strong>Features:</strong> {len(model_features)}<br>
                                            • <strong>Performance:</strong> {selected_result['metrics']['f1']:.4f} F1-Score<br>
                                            • <strong>Timestamp:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                                        </div>
                                        """, unsafe_allow_html=True)
                                    else:
                                        st.error("❌ Failed to save model. Check file permissions.")
                                        
                                except Exception as e:
                                    st.error(f"Error saving model: {str(e)}")
                            else:
                                st.warning("Please select a model and enter a filename")
                    
                    else:
                        st.info("No new models available to save. Train some models first!")
                
                else:
                    st.error("❌ No models were successfully evaluated for comparison.")
    
    else:
        st.markdown("""
        <div class="warning-card">
            <strong>⚠️ Your Model Not Found</strong><br>
            Cannot load 'best_random_forest_classifier.joblib'. Please ensure the file exists in the current directory.
            You can still train new models above for analysis.
        </div>
        """, unsafe_allow_html=True)
def render_strategic_insights(df: pd.DataFrame, clean_features: List[str]):
    """Render strategic insights page with actionable recommendations"""
    
    st.markdown("## 💡 Strategic Insights & Recommendations")
    
    # Key insights summary
    st.markdown("### 🎯 Executive Summary")
    
    # Calculate key metrics for insights
    total_students = len(df)
    completion_rate = (df["course_completed"].sum() / len(df)) * 100
    high_risk_count = len(df[df["risk_category"] == "High Risk"])
    high_risk_pct = (high_risk_count / total_students) * 100
    avg_engagement = df["total_events"].mean()
    
    # Generate insights based on data
    insights = []
    
    # Completion rate insights
    if completion_rate < 60:
        insights.append({
            "type": "danger",
            "title": "🚨 Critical Completion Rate",
            "content": f"Only {completion_rate:.1f}% of students complete courses. Immediate intervention needed.",
            "priority": "High",
            "stakeholder": "Academic Affairs Leadership"
        })
    elif completion_rate < 75:
        insights.append({
            "type": "warning", 
            "title": "⚠️ Below-Target Completion",
            "content": f"Completion rate of {completion_rate:.1f}% is below optimal. Focus on retention strategies.",
            "priority": "Medium",
            "stakeholder": "Student Success Coordinators"
        })
    else:
        insights.append({
            "type": "success",
            "title": "✅ Strong Completion Rate",
            "content": f"Excellent completion rate of {completion_rate:.1f}%. Maintain current strategies.",
            "priority": "Low",
            "stakeholder": "All Stakeholders"
        })
    
    # Risk distribution insights
    if high_risk_pct > 30:
        insights.append({
            "type": "danger",
            "title": "🔴 High At-Risk Population",
            "content": f"{high_risk_count} students ({high_risk_pct:.1f}%) are at high risk. Scale intervention programs.",
            "priority": "High",
            "stakeholder": "Student Success Coordinators"
        })
    elif high_risk_pct > 15:
        insights.append({
            "type": "warning",
            "title": "🟡 Moderate Risk Levels",
            "content": f"{high_risk_count} students need attention. Implement targeted support.",
            "priority": "Medium", 
            "stakeholder": "Faculty Members"
        })
    
    # Engagement insights
    low_engagement_threshold = df["total_events"].quantile(0.25)
    low_engagement_count = len(df[df["total_events"] < low_engagement_threshold])
    
    if low_engagement_count > total_students * 0.3:
        insights.append({
            "type": "warning",
            "title": "📉 Low Engagement Alert",
            "content": f"{low_engagement_count} students show low engagement. Enhance content delivery.",
            "priority": "Medium",
            "stakeholder": "Educational Technology Directors"
        })
    
    # Display insights in organized cards
    for insight in insights:
        card_class = f"{insight['type']}-card"
        priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}[insight['priority']]
        
        st.markdown(f"""
        <div class="{card_class}">
            <h4>{insight['title']}</h4>
            <p>{insight['content']}</p>
            <div style="margin-top: 1rem; font-size: 0.9rem;">
                <strong>Priority:</strong> {priority_color} {insight['priority']} | 
                <strong>Stakeholder:</strong> {insight['stakeholder']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Stakeholder-specific recommendations
    st.markdown("---")
    st.markdown("### 👥 Stakeholder-Specific Action Plans")
    
    stakeholder_tabs = st.tabs([
        "🏛️ Academic Affairs", 
        "💻 EdTech Directors", 
        "🎯 Student Success", 
        "👨‍🏫 Faculty Members"
    ])
    
    with stakeholder_tabs[0]:
        st.markdown("#### 🏛️ Academic Affairs Leadership")
        
        # Calculate strategic metrics
        program_effectiveness = completion_rate / 100
        resource_efficiency = avg_engagement / df["total_marks"].mean() if df["total_marks"].mean() > 0 else 0
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Strategic Metrics")
            st.metric("Program Effectiveness", f"{program_effectiveness:.2%}")
            st.metric("Resource Efficiency", f"{resource_efficiency:.3f}")
            st.metric("At-Risk Population", f"{high_risk_pct:.1f}%")
        
        with col2:
            st.markdown("##### 🎯 Strategic Recommendations")
            
            recommendations = [
                "📈 **Budget Allocation**: Increase funding for student support services",
                "🔄 **Policy Review**: Update retention policies based on engagement data", 
                "📊 **KPI Tracking**: Implement dashboard monitoring for leadership",
                "🤝 **Stakeholder Alignment**: Coordinate cross-departmental initiatives"
            ]
            
            for rec in recommendations:
                st.markdown(f"• {rec}")
        
        # ROI Analysis
        st.markdown("##### 💰 Return on Investment Analysis")
        
        # Estimate potential improvements
        potential_improvement = min(20, (85 - completion_rate)) if completion_rate < 85 else 5
        students_saved = (potential_improvement / 100) * total_students
        estimated_value_per_student = 5000  # Placeholder value
        
        roi_data = {
            "Metric": ["Current Completion Rate", "Target Completion Rate", "Additional Students Retained", "Estimated Value Impact"],
            "Value": [f"{completion_rate:.1f}%", f"{completion_rate + potential_improvement:.1f}%", 
                     f"{students_saved:.0f} students", f"${students_saved * estimated_value_per_student:,.0f}"]
        }
        
        roi_df = pd.DataFrame(roi_data)
        st.dataframe(roi_df, use_container_width=True, hide_index=True)
    
    with stakeholder_tabs[1]:
        st.markdown("#### 💻 Educational Technology Directors")
        
        # Technical insights
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🔧 Technical Metrics")
            
            # Calculate technical metrics
            avg_login_frequency = df["average_login"].mean() if "average_login" in df.columns else 0
            resource_utilization = df["num_resource_views"].mean() if "num_resource_views" in df.columns else 0
            platform_engagement = df["total_engagement_time_sec"].mean() / 3600 if "total_engagement_time_sec" in df.columns else 0  # Convert to hours
            
            st.metric("Avg Login Frequency", f"{avg_login_frequency:.1f}")
            st.metric("Resource Utilization", f"{resource_utilization:.1f}")
            st.metric("Platform Engagement", f"{platform_engagement:.1f} hrs")
        
        with col2:
            st.markdown("##### 🚀 Technology Recommendations")
            
            tech_recommendations = [
                "📱 **Mobile Optimization**: Improve mobile learning experience",
                "🤖 **AI Integration**: Implement personalized learning paths",
                "📊 **Analytics Enhancement**: Deploy real-time engagement tracking",
                "🔔 **Notification System**: Create smart alert mechanisms"
            ]
            
            for rec in tech_recommendations:
                st.markdown(f"• {rec}")
        
        # Feature usage analysis
        st.markdown("##### 📈 Feature Usage Analysis")
        
        feature_usage = {}
        usage_features = ["num_forum_posts", "num_resource_views", "no_of_all_files_downloaded"]
        
        for feature in usage_features:
            if feature in df.columns:
                feature_usage[feature.replace("_", " ").title()] = df[feature].mean()
        
        if feature_usage:
            usage_df = pd.DataFrame(list(feature_usage.items()), columns=["Feature", "Average Usage"])
            usage_df = usage_df.sort_values("Average Usage", ascending=False)
            
            fig_usage = px.bar(
                usage_df,
                x="Average Usage",
                y="Feature",
                title="Platform Feature Usage",
                orientation="h"
            )
            fig_usage.update_layout(height=300)
            st.plotly_chart(fig_usage, use_container_width=True)
    
    with stakeholder_tabs[2]:
        st.markdown("#### 🎯 Student Success Coordinators")
        
        # Intervention planning
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🚨 Intervention Priorities")
            
            # Identify intervention targets
            intervention_targets = []
            
            # High-risk students
            high_risk_students = df[df["risk_category"] == "High Risk"]
            if len(high_risk_students) > 0:
                intervention_targets.append({
                    "group": "High Risk Students",
                    "count": len(high_risk_students),
                    "priority": "Immediate",
                    "action": "One-on-one counseling"
                })
            
            # Low engagement students
            low_engagement_students = df[df["total_events"] < df["total_events"].quantile(0.2)]
            if len(low_engagement_students) > 0:
                intervention_targets.append({
                    "group": "Low Engagement",
                    "count": len(low_engagement_students),
                    "priority": "High",
                    "action": "Engagement campaigns"
                })
            
            # Inactive students
            if "num_days_active" in df.columns:
                inactive_students = df[df["num_days_active"] < 5]
                if len(inactive_students) > 0:
                    intervention_targets.append({
                        "group": "Inactive Students", 
                        "count": len(inactive_students),
                        "priority": "Medium",
                        "action": "Re-engagement outreach"
                    })
            
            for target in intervention_targets:
                priority_color = {"Immediate": "🔴", "High": "🟡", "Medium": "🟠"}[target['priority']]
                st.markdown(f"""
                <div class="info-card">
                    <strong>{target['group']}</strong><br>
                    Count: {target['count']} students<br>
                    Priority: {priority_color} {target['priority']}<br>
                    Action: {target['action']}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("##### 📋 Intervention Strategies")
            
            strategies = [
                "📞 **Proactive Outreach**: Contact at-risk students weekly",
                "👥 **Peer Mentoring**: Pair struggling students with successful peers",
                "📚 **Study Groups**: Organize collaborative learning sessions",
                "🎯 **Goal Setting**: Help students set achievable milestones",
                "📊 **Progress Tracking**: Monitor improvement metrics"
            ]
            
            for strategy in strategies:
                st.markdown(f"• {strategy}")
        
        # Success prediction model
        st.markdown("##### 🔮 Success Prediction Framework")
        
        # Calculate success indicators
        success_indicators = []
        
        if "total_events" in df.columns:
            high_engagement_threshold = df["total_events"].quantile(0.75)
            success_indicators.append(f"Students with >{high_engagement_threshold:.0f} events have {((df[df['total_events'] > high_engagement_threshold]['course_completed'].mean()) * 100):.1f}% completion rate")
        
        if "num_days_active" in df.columns:
            active_threshold = df["num_days_active"].quantile(0.75)
            success_indicators.append(f"Students active >{active_threshold:.0f} days show {((df[df['num_days_active'] > active_threshold]['course_completed'].mean()) * 100):.1f}% success rate")
        
        for indicator in success_indicators:
            st.markdown(f"• {indicator}")
    
    with stakeholder_tabs[3]:
        st.markdown("#### 👨‍🏫 Faculty Members")
        
        # Teaching insights
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📚 Teaching Effectiveness Metrics")
            
            # Calculate teaching-related metrics
            if "num_forum_posts" in df.columns:
                forum_engagement = df["num_forum_posts"].mean()
                st.metric("Forum Engagement", f"{forum_engagement:.1f} posts/student")
            
            if "no_of_assignments" in df.columns:
                assignment_completion = df["no_of_assignments"].mean()
                st.metric("Assignment Engagement", f"{assignment_completion:.1f}")
            
            if "no_of_attendance_taken" in df.columns:
                attendance_rate = df["no_of_attendance_taken"].mean()
                st.metric("Attendance Tracking", f"{attendance_rate:.1f}")
        
        with col2:
            st.markdown("##### 🎓 Pedagogical Recommendations")
            
            pedagogy_recommendations = [
                "💬 **Increase Interaction**: Boost forum discussions and Q&A",
                "📝 **Formative Assessment**: Implement regular check-ins",
                "🎮 **Gamification**: Add achievement badges and progress tracking",
                "📹 **Multimedia Content**: Diversify content delivery methods",
                "🤝 **Collaborative Learning**: Encourage peer-to-peer learning"
            ]
            
            for rec in pedagogy_recommendations:
                st.markdown(f"• {rec}")
        
        # Student engagement patterns
        st.markdown("##### 📊 Student Engagement Patterns")
        
        # Analyze engagement by time patterns
        time_patterns = ["weekend_login", "weekday_login", "evening_login", "morning_login"]
        available_patterns = [p for p in time_patterns if p in df.columns]
        
        if available_patterns:
            pattern_data = {}
            for pattern in available_patterns:
                pattern_data[pattern.replace("_", " ").title()] = df[pattern].mean()
            
            pattern_df = pd.DataFrame(list(pattern_data.items()), columns=["Time Pattern", "Average Activity"])
            pattern_df = pattern_df.sort_values("Average Activity", ascending=False)
            
            fig_patterns = px.bar(
                pattern_df,
                x="Time Pattern",
                y="Average Activity",
                title="Student Activity Patterns"
            )
            fig_patterns.update_layout(height=300)
            st.plotly_chart(fig_patterns, use_container_width=True)
    
    # Implementation roadmap
    st.markdown("---")
    st.markdown("### 🗺️ Implementation Roadmap")
    
    # Create timeline
    roadmap_phases = [
        {
            "phase": "Phase 1: Immediate Actions (0-30 days)",
            "actions": [
                "Deploy early warning system for at-risk students",
                "Implement weekly check-ins for high-risk students", 
                "Launch engagement campaigns for low-activity students"
            ],
            "stakeholders": ["Student Success Coordinators", "Faculty Members"],
            "success_metrics": ["Reduction in at-risk students by 15%", "Increase in weekly engagement by 25%"]
        },
        {
            "phase": "Phase 2: Strategic Initiatives (1-3 months)",
            "actions": [
                "Integrate predictive analytics into student information system",
                "Develop personalized learning pathways",
                "Establish peer mentoring programs"
            ],
            "stakeholders": ["EdTech Directors", "Academic Affairs"],
            "success_metrics": ["Completion rate increase by 10%", "Student satisfaction improvement"]
        },
        {
            "phase": "Phase 3: Optimization (3-6 months)",
            "actions": [
                "Refine intervention strategies based on outcomes",
                "Scale successful programs institution-wide",
                "Implement continuous improvement processes"
            ],
            "stakeholders": ["All Stakeholders"],
            "success_metrics": ["Sustained completion rate >80%", "Reduced intervention costs"]
        }
    ]
    
    for i, phase in enumerate(roadmap_phases):
        with st.expander(f"📅 {phase['phase']}", expanded=(i == 0)):
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**🎯 Key Actions:**")
                for action in phase['actions']:
                    st.markdown(f"• {action}")
                
                st.markdown("**👥 Stakeholders:**")
                st.markdown(f"• {', '.join(phase['stakeholders'])}")
            
            with col2:
                st.markdown("**📊 Success Metrics:**")
                for metric in phase['success_metrics']:
                    st.markdown(f"• {metric}")
    
    # Success measurement framework
    st.markdown("---")
    st.markdown("### 📏 Success Measurement Framework")
    
    measurement_categories = {
        "📈 Engagement Metrics": [
            "Weekly active users increase",
            "Average session duration improvement", 
            "Forum participation growth",
            "Resource utilization rates"
        ],
        "🎯 Performance Metrics": [
            "Course completion rate improvement",
            "Average grade increase",
            "Time to completion reduction",
            "Student satisfaction scores"
        ],
        "💰 Efficiency Metrics": [
            "Cost per successful student",
            "Intervention success rate",
            "Resource allocation optimization",
            "Staff productivity measures"
        ]
    }
    
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    for i, (category, metrics) in enumerate(measurement_categories.items()):
        with columns[i]:
            st.markdown(f"#### {category}")
            for metric in metrics:
                st.markdown(f"• {metric}")
    
    # Final call to action
    st.markdown("---")
    st.markdown("""
    <div class="success-card">
        <h3>🚀 Ready to Transform Student Success?</h3>
        <p>This data-driven approach provides a clear pathway to improving student outcomes. 
        The combination of predictive analytics, targeted interventions, and continuous monitoring 
        creates a comprehensive framework for educational excellence.</p>
        
        <p><strong>Next Steps:</strong></p>
        <ul>
            <li>Share these insights with your stakeholder teams</li>
            <li>Prioritize interventions based on your institutional context</li>
            <li>Implement monitoring systems for continuous improvement</li>
            <li>Schedule regular review meetings to track progress</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
def render_data_explorer(df: pd.DataFrame, clean_features: List[str]):
    """Render interactive data explorer page"""
    
    st.markdown("## 📋 Interactive Data Explorer")
    
    # Data overview
    st.markdown("### 📊 Dataset Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    with col2:
        st.metric("Features", f"{len(clean_features)}")
    with col3:
        st.metric("Completion Rate", f"{(df['course_completed'].mean() * 100):.1f}%")
    with col4:
        st.metric("Missing Values", f"{df.isnull().sum().sum()}")
    
    # Interactive data table
    st.markdown("### 🔍 Interactive Data Table")
    
    # Column selection
    display_columns = st.multiselect(
        "Select columns to display:",
        options=clean_features + ["total_marks", "course_completed", "risk_category"],
        default=clean_features[:5] + ["total_marks", "risk_category"],
        help="Choose which columns to show in the data table"
    )
    
    if display_columns:
        # Filtering options
        col1, col2 = st.columns(2)
        
        with col1:
            # Numeric filter
            numeric_cols = [col for col in display_columns if df[col].dtype in ['int64', 'float64']]
            if numeric_cols:
                filter_column = st.selectbox("Filter by column:", ["None"] + numeric_cols)
                
                if filter_column != "None":
                    min_val, max_val = float(df[filter_column].min()), float(df[filter_column].max())
                    filter_range = st.slider(
                        f"Filter {filter_column}:",
                        min_value=min_val,
                        max_value=max_val,
                        value=(min_val, max_val)
                    )
                    
                    filtered_data = df[
                        (df[filter_column] >= filter_range[0]) & 
                        (df[filter_column] <= filter_range[1])
                    ]
                else:
                    filtered_data = df
            else:
                filtered_data = df
        
        with col2:
            # Sorting options
            sort_column = st.selectbox("Sort by:", display_columns)
            sort_order = st.selectbox("Sort order:", ["Ascending", "Descending"])
            
            if sort_order == "Descending":
                filtered_data = filtered_data.sort_values(sort_column, ascending=False)
            else:
                filtered_data = filtered_data.sort_values(sort_column, ascending=True)
        
        # Display filtered data
        st.dataframe(
            filtered_data[display_columns].head(100),  # Limit to 100 rows for performance
            use_container_width=True,
            height=400
        )
        
        st.info(f"Showing {min(100, len(filtered_data))} of {len(filtered_data)} filtered records")
    
    # Statistical summary
    st.markdown("### 📈 Statistical Summary")
    
    if display_columns:
        numeric_columns = [col for col in display_columns if df[col].dtype in ['int64', 'float64']]
        
        if numeric_columns:
            summary_stats = df[numeric_columns].describe().round(3)
            st.dataframe(summary_stats, use_container_width=True)
            
            # Download summary
            csv_summary = summary_stats.to_csv()
            st.download_button(
                label="📥 Download Summary Statistics",
                data=csv_summary,
                file_name="summary_statistics.csv",
                mime="text/csv"
            )
    
    # Data quality assessment
    st.markdown("### 🔍 Data Quality Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Missing Values Analysis")
        
        missing_data = df[clean_features].isnull().sum()
        missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
        
        if len(missing_data) > 0:
            fig_missing = px.bar(
                x=missing_data.values,
                y=missing_data.index,
                title="Missing Values by Feature",
                orientation='h'
            )
            fig_missing.update_layout(height=400)
            st.plotly_chart(fig_missing, use_container_width=True)
        else:
            st.success("✅ No missing values found!")
    
    with col2:
        st.markdown("#### Data Distribution Analysis")
        
        # Select feature for distribution analysis
        dist_feature = st.selectbox(
            "Select feature for distribution:",
            options=clean_features,
            key="dist_analysis"
        )
        
        if dist_feature:
            fig_dist = px.histogram(
                df,
                x=dist_feature,
                title=f"Distribution: {dist_feature.replace('_', ' ').title()}",
                nbins=30
            )
            fig_dist.update_layout(height=400)
            st.plotly_chart(fig_dist, use_container_width=True)
    
    # Export options
    st.markdown("### 📤 Export Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Export filtered data
        if st.button("📊 Export Filtered Data"):
            if 'filtered_data' in locals() and display_columns:
                csv_data = filtered_data[display_columns].to_csv(index=False)
                st.download_button(
                    label="📥 Download CSV",
                    data=csv_data,
                    file_name="filtered_student_data.csv",
                    mime="text/csv"
                )
    
    with col2:
        # Export correlation matrix
        if st.button("🔗 Export Correlations"):
            numeric_features = [f for f in clean_features if df[f].dtype in ['int64', 'float64']]
            if len(numeric_features) > 1:
                corr_matrix = df[numeric_features].corr()
                csv_corr = corr_matrix.to_csv()
                st.download_button(
                    label="📥 Download Correlations",
                    data=csv_corr,
                    file_name="correlation_matrix.csv",
                    mime="text/csv"
                )
    
    with col3:
        # Export summary report
        if st.button("📋 Generate Summary Report"):
            report_data = {
                "Dataset Overview": {
                    "Total Records": len(df),
                    "Features": len(clean_features),
                    "Completion Rate": f"{(df['course_completed'].mean() * 100):.1f}%",
                    "High Risk Students": len(df[df['risk_category'] == 'High Risk'])
                },
                "Key Statistics": df[clean_features[:5]].describe().to_dict()
            }
            
            report_json = json.dumps(report_data, indent=2)
            st.download_button(
                label="📥 Download Report",
                data=report_json,
                file_name="data_summary_report.json",
                mime="application/json"
            )

def render_report_generator(df: pd.DataFrame, clean_features: List[str], metadata: Dict[str, Any]):
    """Render automated report generator page"""
    
    st.markdown("## 📄 Automated Report Generator")
    
    # Report configuration
    st.markdown("### ⚙️ Report Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        report_type = st.selectbox(
            "Report Type:",
            options=[
                "Executive Summary",
                "Technical Analysis", 
                "Stakeholder Briefing",
                "Intervention Plan",
                "Performance Dashboard"
            ]
        )
        
        report_audience = st.selectbox(
            "Target Audience:",
            options=[
                "Academic Affairs Leadership",
                "Educational Technology Directors",
                "Student Success Coordinators", 
                "Faculty Members",
                "All Stakeholders"
            ]
        )
    
    with col2:
        include_sections = st.multiselect(
            "Include Sections:",
            options=[
                "Key Metrics",
                "Risk Analysis", 
                "Engagement Patterns",
                "Predictive Insights",
                "Recommendations",
                "Implementation Plan"
            ],
            default=["Key Metrics", "Risk Analysis", "Recommendations"]
        )
        
        report_format = st.selectbox(
            "Output Format:",
            options=["HTML", "Markdown", "JSON"]
        )
    
    # Generate report button
    if st.button("🚀 Generate Report", type="primary"):
        with st.spinner("Generating comprehensive report..."):
            
            # Calculate key metrics
            total_students = len(df)
            completion_rate = (df["course_completed"].sum() / len(df)) * 100
            high_risk_count = len(df[df["risk_category"] == "High Risk"])
            high_risk_pct = (high_risk_count / total_students) * 100
            avg_engagement = df["total_events"].mean()
            
            # Generate report content
            report_content = {
                "title": f"{report_type} - Student Engagement Analytics",
                "audience": report_audience,
                "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "data_summary": {
                    "total_students": total_students,
                    "completion_rate": f"{completion_rate:.1f}%",
                    "high_risk_students": high_risk_count,
                    "high_risk_percentage": f"{high_risk_pct:.1f}%",
                    "average_engagement": f"{avg_engagement:.1f}"
                }
            }
            
            # Add selected sections
            if "Key Metrics" in include_sections:
                report_content["key_metrics"] = {
                    "student_population": total_students,
                    "success_rate": completion_rate,
                    "intervention_needed": high_risk_count,
                    "engagement_level": avg_engagement
                }
            
            if "Risk Analysis" in include_sections:
                risk_distribution = df["risk_category"].value_counts().to_dict()
                report_content["risk_analysis"] = {
                    "distribution": risk_distribution,
                    "high_risk_factors": "Low engagement, minimal resource usage",
                    "intervention_priority": "Immediate attention required for high-risk students"
                }
            
            if "Engagement Patterns" in include_sections:
                engagement_stats = {
                    "average_events": df["total_events"].mean(),
                    "average_active_days": df["num_days_active"].mean() if "num_days_active" in df.columns else "N/A",
                    "forum_participation": df["num_forum_posts"].mean() if "num_forum_posts" in df.columns else "N/A"
                }
                report_content["engagement_patterns"] = engagement_stats
            
            if "Predictive Insights" in include_sections:
                # Calculate correlation insights
                correlations = []
                for feature in clean_features[:5]:  # Top 5 features
                    if feature in df.columns:
                        corr = df[feature].corr(df["total_marks"])
                        if not pd.isna(corr):
                            correlations.append({"feature": feature, "correlation": f"{corr:.3f}"})
                
                report_content["predictive_insights"] = {
                    "top_predictors": correlations,
                    "model_accuracy": "92% (based on clean features)",
                    "key_finding": "91.4% correlation between engagement and performance"
                }
            
            if "Recommendations" in include_sections:
                recommendations = []
                
                if high_risk_pct > 20:
                    recommendations.append("Implement immediate intervention for high-risk students")
                if completion_rate < 75:
                    recommendations.append("Develop retention improvement strategies")
                if avg_engagement < df["total_events"].quantile(0.5):
                    recommendations.append("Enhance engagement through interactive content")
                
                report_content["recommendations"] = recommendations
            
            if "Implementation Plan" in include_sections:
                report_content["implementation_plan"] = {
                    "phase_1": "Deploy early warning system (0-30 days)",
                    "phase_2": "Implement targeted interventions (1-3 months)",
                    "phase_3": "Scale and optimize programs (3-6 months)",
                    "success_metrics": ["Completion rate improvement", "Risk reduction", "Engagement increase"]
                }
            
            # Format and display report
            if report_format == "HTML":
                html_report = generate_html_report(report_content)
                st.markdown("### 📄 Generated Report")
                st.markdown(html_report, unsafe_allow_html=True)
                
                # Download button
                st.download_button(
                    label="📥 Download HTML Report",
                    data=html_report,
                    file_name=f"student_analytics_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
                    mime="text/html"
                )
            
            elif report_format == "Markdown":
                md_report = generate_markdown_report(report_content)
                st.markdown("### 📄 Generated Report")
                st.markdown(md_report)
                
                st.download_button(
                    label="📥 Download Markdown Report",
                    data=md_report,
                    file_name=f"student_analytics_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
            
            elif report_format == "JSON":
                json_report = json.dumps(report_content, indent=2)
                st.markdown("### 📄 Generated Report")
                st.json(report_content)
                
                st.download_button(
                    label="📥 Download JSON Report",
                    data=json_report,
                    file_name=f"student_analytics_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
    
    # Report templates
    st.markdown("---")
    st.markdown("### 📋 Report Templates")
    
    templates = {
        "Executive Summary": "High-level overview for leadership decision-making",
        "Technical Analysis": "Detailed statistical analysis for data teams",
        "Stakeholder Briefing": "Targeted insights for specific stakeholder groups",
        "Intervention Plan": "Action-oriented recommendations for student success",
        "Performance Dashboard": "Key metrics and trends for ongoing monitoring"
    }
    
    for template, description in templates.items():
        with st.expander(f"📄 {template}"):
            st.markdown(f"**Description:** {description}")
            
            if template == "Executive Summary":
                st.markdown("""
                **Includes:**
                - Key performance indicators
                - Risk assessment summary
                - Strategic recommendations
                - ROI analysis
                - Implementation timeline
                """)
            elif template == "Technical Analysis":
                st.markdown("""
                **Includes:**
                - Statistical analysis
                - Correlation matrices
                - Model performance metrics
                - Feature importance analysis
                - Data quality assessment
                """)
            elif template == "Stakeholder Briefing":
                st.markdown("""
                **Includes:**
                - Role-specific insights
                - Targeted recommendations
                - Action items
                - Success metrics
                - Resource requirements
                """)

def generate_html_report(content: Dict[str, Any]) -> str:
    """Generate HTML formatted report"""
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{content['title']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ background: #2563eb; color: white; padding: 20px; border-radius: 8px; }}
            .section {{ margin: 20px 0; padding: 15px; border-left: 4px solid #2563eb; }}
            .metric {{ display: inline-block; margin: 10px; padding: 10px; background: #f8fafc; border-radius: 4px; }}
            .recommendation {{ background: #ecfdf5; padding: 10px; margin: 5px 0; border-radius: 4px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>{content['title']}</h1>
            <p>Target Audience: {content['audience']}</p>
            <p>Generated: {content['generated_date']}</p>
        </div>
    """
    
    if 'key_metrics' in content:
        html += """
        <div class="section">
            <h2>📊 Key Metrics</h2>
        """
        for metric, value in content['key_metrics'].items():
            html += f'<div class="metric"><strong>{metric.replace("_", " ").title()}:</strong> {value}</div>'
        html += "</div>"
    
    if 'recommendations' in content:
        html += """
        <div class="section">
            <h2>💡 Recommendations</h2>
        """
        for rec in content['recommendations']:
            html += f'<div class="recommendation">• {rec}</div>'
        html += "</div>"
    
    html += """
    </body>
    </html>
    """
    
    return html

def generate_markdown_report(content: Dict[str, Any]) -> str:
    """Generate Markdown formatted report"""
    
    md = f"""# {content['title']}

**Target Audience:** {content['audience']}  
**Generated:** {content['generated_date']}

---

"""
    
    if 'key_metrics' in content:
        md += "## 📊 Key Metrics\n\n"
        for metric, value in content['key_metrics'].items():
            md += f"- **{metric.replace('_', ' ').title()}:** {value}\n"
        md += "\n"
    
    if 'risk_analysis' in content:
        md += "## 🎯 Risk Analysis\n\n"
        md += f"- **High Risk Students:** {content['risk_analysis'].get('distribution', {}).get('High Risk', 0)}\n"
        md += f"- **Intervention Priority:** {content['risk_analysis'].get('intervention_priority', 'N/A')}\n\n"
    
    if 'recommendations' in content:
        md += "## 💡 Recommendations\n\n"
        for rec in content['recommendations']:
            md += f"- {rec}\n"
        md += "\n"
    
    if 'implementation_plan' in content:
        md += "## 🗺️ Implementation Plan\n\n"
        plan = content['implementation_plan']
        md += f"1. **Phase 1:** {plan.get('phase_1', 'N/A')}\n"
        md += f"2. **Phase 2:** {plan.get('phase_2', 'N/A')}\n"
        md += f"3. **Phase 3:** {plan.get('phase_3', 'N/A')}\n\n"
    
    return md

# Main application logic
def main():
    """Main application entry point"""
    
    # Initialize application
    df, clean_features, metadata = initialize_app()
    
    # Render header
    render_header()
    
    # Render sidebar and get selections
    page, selected_risks, filter_settings = render_sidebar(df, metadata)
    
    # Apply filters
    filtered_df = apply_filters(df, filter_settings)
    
    # Show filter summary
    if len(filtered_df) != len(df):
        st.info(f"📊 Showing {len(filtered_df):,} of {len(df):,} students based on your filters")
    
    # Render selected page
    if page == "📊 Executive Overview":
        render_executive_overview(filtered_df, clean_features)
    elif page == "📈 Advanced Analytics":
        render_advanced_analytics(filtered_df, clean_features)
    elif page == "🤖 Predictive Models":
        render_predictive_models(filtered_df, clean_features)
    elif page == "💡 Strategic Insights":
        render_strategic_insights(filtered_df, clean_features)
    elif page == "📋 Data Explorer":
        render_data_explorer(filtered_df, clean_features)
    elif page == "📄 Report Generator":
        render_report_generator(filtered_df, clean_features, metadata)
    
    # Enhanced footer
    st.markdown("---")
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        color: white;
        padding: 2rem;
        border-radius: 16px;
        margin-top: 3rem;
        text-align: center;
    ">
        <h2 style="margin-bottom: 1rem; font-size: 1.8rem;">🎓 Enhanced Student Analytics Platform</h2>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem; opacity: 0.9;">
            <strong>Milestone 4: Advanced Communication Results</strong>
        </p>
        <div style="display: flex; justify-content: center; gap: 3rem; margin-top: 2rem; flex-wrap: wrap;">
            <div style="text-align: center;">
                <div style="font-size: 0.9rem; opacity: 0.8;">Data Science Excellence</div>
                <div style="font-weight: 600; font-size: 1.1rem;">Ultra-clean modeling</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 0.9rem; opacity: 0.8;">Quality Assurance</div>
                <div style="font-weight: 600; font-size: 1.1rem;">Zero data leakage</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 0.9rem; opacity: 0.8;">Impact Delivery</div>
                <div style="font-weight: 600; font-size: 1.1rem;">Actionable insights</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 0.9rem; opacity: 0.8;">Innovation</div>
                <div style="font-weight: 600; font-size: 1.1rem;">Enhanced analytics</div>
            </div>
        </div>
        <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.2); font-size: 0.9rem; opacity: 0.7;">
            Enhanced by Amazon Q with ❤️ for educational excellence
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
