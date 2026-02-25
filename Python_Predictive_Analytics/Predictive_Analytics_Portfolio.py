"""
TECHNICAL RIGOR SERIES: 04 - Predictive Analytics & ETL Logic
Focus: Machine Learning Pipeline, Data Cleaning, and Statistical Modeling
Application: Customer Churn Prediction & Supply Chain Optimization
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# --- SCENARIO 1: Automated Data Cleaning (ETL Logic) ---
# Logic: Handling missing values and normalizing formats for 1,000+ daily records.
def clean_enterprise_data(df):
    # Filling missing numerical values with median to handle outliers
    df['salary'] = df['salary'].fillna(df['salary'].median())
    # Standardizing categorical strings for SQL consistency
    df['department'] = df['department'].str.strip().str.upper()
    return df

# --- SCENARIO 2: Feature Engineering for Churn Prediction ---
# Logic: Creating 'Tenure' and 'Engagement Score' to identify high-risk customers.
def engineer_churn_features(df):
    df['engagement_score'] = df['total_transactions'] / df['months_active']
    df['is_high_risk'] = np.where(df['days_since_last_login'] > 30, 1, 0)
    return df

# --- SCENARIO 3: Machine Learning Model (Random Forest) ---
# Logic: Building a binary classification model to identify churn patterns.
def train_churn_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling features for better model convergence
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X_train_scaled, y_train)
    
    # Performance Evaluation (Proving the "Precision" mentioned in resume)
    predictions = model.predict(scaler.transform(X_test))
    print(classification_report(y_test, predictions))
    return model

# --- SCENARIO 4: Supply Chain Delay Risk Analysis ---
# Logic: Using Statistical methods to identify bottlenecks in logistics data.
def identify_logistics_bottlenecks(df):
    # Identifying routes where average delay is 25% higher than the mean
    mean_delay = df['delay_minutes'].mean()
    bottleneck_routes = df[df['delay_minutes'] > (mean_delay * 1.25)]
    return bottleneck_routes
