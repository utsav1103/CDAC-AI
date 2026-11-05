"""
Title: Employee Productivity & Analytics Lifecycle 
Description: Fill in the TODO sections across the 5 lifecycle phases.

"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, scikit-learn LinearRegression, and metrics
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score , mean_absolute_error, mean_squared_error

df = pd.read_csv("employee_productivity.csv")


def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery & Data Setup (5 Marks)
    - Goal: Load 'employee_productivity.csv' and inspect structure.
    - Check for null values and print summary info.
    """
    print("\n[PHASE 1] Discovery & Data Setup")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    # TODO: Print first 5 rows and verify shape
    print(df.head())
    print(df.shape)
    # TODO: Check for missing values
    print(df.isnull().sum())
    return df
    


def phase_2_descriptive_statistics(df):
    """
    [Phase 2] Descriptive Statistics & Data Measures 
    - Goal: Compute measures of central tendency and dispersion 
      for 'Weekly_Tasks_Completed'.
    - Check for potential outliers using IQR method.
    """
    print("\n[PHASE 2] Descriptive Statistics ")
    print("-" * 65)
    # TODO: Calculate Mean, Median, Std Dev, and IQR for Weekly_Tasks_Completed
    task = df['Weekly_Tasks_Completed']
    print(task.mean())
    print(task.median())
    print(task.std())
    Q1 = task.quantile(0.25)
    Q3 = task.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 0.5 * IQR
    upper_bound = Q3 + 0.5 * IQR

    outliers = task[(task < lower_bound) | (task > upper_bound)]

    # TODO: Identify any values falling outside 1.5 * IQR bounds
    print("Outliers:")
    print(outliers)
    return df

def phase_3_bivariate_association(df):
    """
    [Phase 3] Bivariate Association & Correlation 
    - Goal: Examine relationships between Training Hours, Experience, 
      and Tasks Completed.
    - Compute Pearson correlation matrix.
    """
    print("\n[PHASE 3] Bivariate Association ")
    print("-" * 65)
    # TODO: Select numeric columns and compute Pearson correlation matrix
    # TODO: Highlight the correlation between Training_Hours and Weekly_Tasks_Completed
    numeric_cols = ["Training_Hours","Years_Experience","Weekly_Tasks_Completed","Performance_Rating"]

    corr_matrix = df[numeric_cols].corr(method="pearson")
    print(corr_matrix)\

    correlation = corr_matrix.loc["Training_Hours", "Weekly_Tasks_Completed"]
    print(correlation)


def phase_4_predictive_modeling(df):
    """
    [Phase 4] Predictive Analytics & Regression Modeling 
    - Goal: Predict 'Weekly_Tasks_Completed' based on 'Training_Hours'.
    - Train a Simple Linear Regression model.
    """
    print("\n[PHASE 4] Predictive Modeling ")
    print("-" * 65)
    # TODO: Set X = df[['Training_Hours']] and y = df['Weekly_Tasks_Completed']
    # TODO: Fit Linear Regression model and output slope & intercept
    X = df[["Training_Hours"]]
    y = df["Weekly_Tasks_Completed"]

    model = LinearRegression()
    model.fit(X, y)
    print(model.coef_[0])
    print(model.intercept_)

    predictions = model.predict(X)
    result = pd.DataFrame({
        "Actual": y,
        "Predicted": predictions
    })
    print(result)
    return model , predictions , y

def phase_5_evaluation_and_reporting(model, predictions, y):
    """
    [Phase 5] Evaluation & Prescriptive Recommendation (5 Marks)
    - Goal: Evaluate model using R-squared and MAE.
    - Provide operational HR recommendations based on data.
    """
    print("\n[PHASE 5] Evaluation & HR Recommendations (5 Marks)")
    print("-" * 65)
    # TODO: Calculate R2 score and Mean Absolute Error (MAE)
    # TODO: Print prescriptive action item for employee training investments
    r2 = r2_score(y,predictions)
    mae = mean_absolute_error(y,predictions)
    print("R-squared:", r2)
    print("Mean Absolute Error:", mae)
    


def run_analytics_lifecycle():
    """
    Facade Orchestrator function.
    """
    print("=" * 65)
    print("STARTING EMPLOYEE ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 65)
    
    # Executing phases chronologically
    df = phase_1_discovery_and_setup()
    phase_2_descriptive_statistics(df)
    phase_3_bivariate_association(df)
    model, predictions, y = phase_4_predictive_modeling(df)
    phase_5_evaluation_and_reporting(model, predictions, y)


if __name__ == "__main__":
    run_analytics_lifecycle()