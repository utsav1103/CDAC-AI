"""
Title: End-to-End Data Analytics Lifecycle
Description: A modular Python script demonstrating business discovery, 
             data preparation, exploration, statistics, and predictive modeling.
"""

# ==========================================
# IMPORTS (Libraries for Data, Stats, & Viz)
# ==========================================
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

df = pd.read_csv("coffee_shop_data.csv")

# ==========================================
# SUB-STEP FUNCTIONS (The Lifecycle Phases)
# ==========================================

def phase_1_discovery_and_setup():
    """
    Module 1: Foundations, Business Understanding & Setup
    - Define business objective (e.g., Coffee Shop Revenue Analysis).
    - Load the 25-record real-world CSV dataset.
    - Initial inspection (head, info, missing values).
  
    """
    print("Executing Phase 1: Discovery & Data Setup...")
    # TODO: Load dataset using pandas
    # TODO: Perform basic inspection (shape, data types, missing values)
    df = pd.read_csv('coffee_shop_data.csv')
    print(df.head())
    print(df.shape)
    print(df.dtypes)
    df.info()
    print(df.isnull().sum())

    return df



def phase_2_descriptive_statistics(df):
    """
    Module 2: Descriptive Statistics & Data Measures
    - Calculate Central Tendency (Mean, Median, Mode).
    - Calculate Dispersion (Standard Deviation, Variance, IQR, Range).
    - Check Distribution Shape & Outliers.
  
    """
    print("Executing Phase 2: Descriptive Statistics & Measures...")
    # TODO: Compute summary statistics (mean, median, std, IQR)
    # TODO: Identify and handle any outliers
    numeric_cols = ["Temperature_C","Foot_Traffic","Marketing_Spend_USD","Daily_Revenue_USD"]

    print("\n Centeral Tendency Measures:")
    print("\n Mean:",df[numeric_cols].mean())
    print("\n Median:",df[numeric_cols].median())
    print("\n Mode:",df[numeric_cols].mode().iloc[0])
    print("\n Standard Deviation:", df[numeric_cols].std())
    print("\n variance:", df[numeric_cols].var())
    print("\n Range:", df[numeric_cols].max() - df[numeric_cols].min())

    Q1 = df[numeric_cols].quantile(0.25)
    Q3= df[numeric_cols].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = (df[numeric_cols] < lower_bound) | (df[numeric_cols] > upper_bound)
    print("\n Outliers:\n", outliers.sum())
    # boxplot
    plt.figure(figsize=(10,6))
    plt.title("Boxplot for Numeric Columns")
    sns.boxplot(data=df[numeric_cols])
    plt.tight_layout()
    plt.show()
    return df

def phase_3_bivariate_association(df):
    """
    Module 4: Bivariate & Multivariate Association
    - Analyze relationships between variables (e.g., Marketing Spend vs. Revenue).
    - Compute Covariance and Pearson Correlation Matrix.
    - Generate exploratory visualizations (Scatter plots, Correlation heatmap).
  
    """
    print("Executing Phase 3: Bivariate Association & Visualization...")
    # TODO: Compute correlation matrix
    # TODO: Plot correlation heatmap and scatter plots
    numerical_cols = ["Temperature_C","Foot_Traffic","Marketing_Spend_USD","Daily_Revenue_USD"]

    covariance_matrix = df[numerical_cols].cov()
    print(covariance_matrix)

    corr_matrix = df[numerical_cols].corr(method='pearson')
    print(corr_matrix)

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm',linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

    ## scatter plots
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x = "Marketing_Spend_USD",
        y = "Daily_Revenue_USD",
    )
    plt.title("Marketing Spend vs Daily Revenue")
    plt.xlabel("Marketing Spend (USD)")
    plt.ylabel("Daily Revenue (USD)")
    plt.tight_layout()
    plt.show()

def phase_4_predictive_modeling(df):
    """
    Module 6 & 8: Predictive Analytics & Regression Modeling
    - Set up a simple predictive model (e.g., Simple Linear Regression).
    - Train the model on independent variables to predict revenue.
    - Establish a baseline evaluation.
   
    """
    print("Executing Phase 4: Predictive Modeling...")
    # TODO: Define features (X) and target (y)
    # TODO: Fit a simple linear regression model
    # TODO: Extract model coefficients and intercept
    X = df[["Temperature_C", "Foot_Traffic", "Marketing_Spend_USD"]]
    y = df["Daily_Revenue_USD"]

    # creating linear regression model
    model = LinearRegression()
    model.fit(X, y)

    #extracting coefficients and intercept
    print("Model Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)

    #predict 
    predictions = model.predict(X)

    results = pd.DataFrame({
        "Actual":y,
        "Predicted":predictions
    })
    print(results)
    return model,y,predictions


def phase_5_evaluation_and_reporting(model, y, predictions):
    """
    Module 6 & 7: Model Evaluation, Generalization & Business Decision
    - Evaluate model performance (e.g., R-squared, Mean Absolute Error).
    - Discuss generalization and overfitting risks on small data.
    - Translate technical findings into prescriptive business recommendations.
    [Allocation: 5 Marks]
    """
    print("Executing Phase 5: Evaluation & Business Action...")
    # TODO: Calculate evaluation metrics
    # TODO: Print final business recommendations based on findings
    r2 = r2_score(y,predictions)
    mae = mean_absolute_error(y,predictions)
    mse = mean_squared_error(y,predictions)

    print(f"R-squared: {r2}")
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")

    return {"R-squared": r2, "Mean Absolute Error": mae, "Mean Squared Error": mse}
# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_analytics_lifecycle():
    """
    Facade function that coordinates the entire data analytics 
    lifecycle in chronological order.
    """
    print("=" * 60)
    print("STARTING COMPLETE DATA ANALYTICS LIFECYCLE (Out of 40 Marks)")
    print("=" * 60)
    
    phase_1_discovery_and_setup()
    print("-" * 60)
    
    phase_2_descriptive_statistics(df)
    print("-" * 60)
    
    phase_3_bivariate_association(df)
    print("-" * 60)
    
    model,y,predictions = phase_4_predictive_modeling(df)
    print("-" * 60)
    
    metrics = phase_5_evaluation_and_reporting(model, y, predictions)
    
    print("=" * 60)
    print("ANALYTICS LIFECYCLE COMPLETED SUCCESSFULLY")
    print("=" * 60)


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_analytics_lifecycle()