"""
Title: Unsupervised Cricket Player Role Segmentation 
Description: A modular Python exercise script for loading cricket statistics, 
             scaling features, training a K-Means clustering model to group 
             players into functional roles (Batsmen, Bowlers, All-Rounders), 
             evaluating clusters, and persisting artifacts using joblib.
"""

# Step 0: Import necessary libraries
# TODO: Import pandas, numpy, StandardScaler from sklearn.preprocessing, 
#       KMeans from sklearn.cluster, silhouette_score from sklearn.metrics, and joblib
import pandas as pd
import numpy as np
import joblib

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def phase_1_discovery_and_setup():
    """
    [Phase 1] Discovery, Setup & Feature Selection
    - Goal: Load 'cricket_player_stats.csv' and inspect structure.
    - Separate player names/identifiers from numeric statistics.
    - Select numeric features required for role clustering.
    """
    print("\n[PHASE 1] Discovery & Feature Selection")
    print("-" * 65)
    # TODO: Load CSV file using pandas
    df = pd.read_csv("cricket_player_stats.csv")
    # TODO: Retain 'player_name' for final profiling
    player_names = df["player_name"]
    # TODO: Select numerical features (e.g., 'runs_scored', 'batting_average', 'wickets_taken', 'bowling_economy')
    X = df[["runs_scored","batting_average","wickets_taken","bowling_economy"]]
    print("DATASET SHAPE:",df.shape)
    #print(player_names)
    print(df.head())
    return X,df

def phase_2_feature_scaling(X):
    """
    [Phase 2] Unsupervised Feature Scaling
    - Goal: Fit StandardScaler on performance metrics to equalize feature weightings.
    """
    print("\n[PHASE 2] Unsupervised Feature Scaling")
    print("-" * 65)
    # TODO: Initialize StandardScaler()
    scaler = StandardScaler()
    # TODO: Fit and transform features X into X_scaled
    X_scaled = scaler.fit_transform(X)
    print(X_scaled)
    print(X_scaled.shape)

    return X_scaled,scaler


def phase_3_kmeans_model_induction(X_scaled, df_original):
    """
    [Phase 3] K-Means Model Induction
    - Goal: Train KMeans model setting n_clusters=3 (Batsmen, Bowlers, All-Rounders).
    - Fit model to scaled data and assign cluster labels back to dataset.
    """
    print("\n[PHASE 3] K-Means Model Induction & Labeling")
    print("-" * 65)
    # TODO: Instantiate KMeans(n_clusters=3, random_state=42)
    model = KMeans(n_clusters=3,random_state=42)
    # TODO: Fit model and generate cluster labels using .fit_predict(X_scaled)
    labels = model.fit_predict(X_scaled)
    df_original["cluster_id"] = labels
    print(labels)
    print(df_original[["player_name","cluster_id"]])

    return model,labels,df_original


def phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered):
    """
    [Phase 4] Cluster Evaluation & Role Profiling
    - Goal: Calculate Silhouette Score to measure cluster separation.
    - Calculate average statistics per cluster and translate centroids into cricket roles.
    """
    print("\n[PHASE 4] Cluster Evaluation & Role Profiling")
    print("-" * 65)
    # TODO: Compute silhouette_score(X_scaled, labels)
    score = silhouette_score(X_scaled,labels)
    print("Silhouette Score:", score)
    # TODO: Group df_clustered by 'cluster_id' and compute mean statistics to interpret roles
    profile = df_clustered.groupby("cluster_id")[[
        "runs_scored",
        "batting_average",
        "wickets_taken",
        "bowling_economy"
    ]].mean()
    print(profile)

    return profile


def phase_5_joblib_model_persistence(model, scaler, feature_names):
    """
    [Phase 5] Unsupervised Model Persistence with Joblib
    - Goal: Save the trained KMeans model and scaler to disk using joblib.
    - Test loading artifacts to assign a new player profile to a role cluster.
    """
    print("\n[PHASE 5] Model Persistence with Joblib")
    print("-" * 65)
    # TODO: Save model, scaler, and feature list using joblib.dump()
    joblib.dump(model,"cricket_kmeans_model.joblib")
    joblib.dump(scaler,"cricket_scaler.joblib")
    joblib.dump(feature_names,"cricket_feature_names.joblib")
    print("Modle , Scaler and Feature Names Saved Successfully")
    # TODO: Load artifacts using joblib.load() and predict the cluster for a new player profile
    loaded_model = joblib.load("cricket_kmeans_model.joblib")
    loaded_scaler = joblib.load("cricket_scaler.joblib")
    loaded_features = joblib.load("cricket_feature_names.joblib")
    print("saved files loaded successfully")

    sample_player = pd.DataFrame(
        [[6000, 40.0, 80, 5.5]],
        columns=loaded_features
    )

    # Step 4: Scale new player data
    sample_scaled = loaded_scaler.transform(sample_player)

    # Step 5: Predict cluster
    cluster = loaded_model.predict(sample_scaled)

    print("\nNew Player Profile:")
    print(sample_player)

    print("Predicted Cluster:", cluster[0])

# ==========================================
# THE FACADE FUNCTION (Orchestrator)
# ==========================================

def run_cricket_clustering_pipeline():
    """
    Facade function coordinating the cricket player segmentation pipeline.
    """
    print("=" * 65)
    print("STARTING CRICKET PLAYER ROLE CLUSTERING LIFECYCLE (K-Means)")
    print("=" * 65)
    
    # Executing phases chronologically
    X, df_original = phase_1_discovery_and_setup()
    X_scaled, scaler = phase_2_feature_scaling(X)
    model, labels, df_clustered = phase_3_kmeans_model_induction(X_scaled, df_original)
    phase_4_cluster_evaluation_and_profiling(X_scaled, labels, df_clustered)
    phase_5_joblib_model_persistence(model, scaler, list(X.columns))


# ==========================================
# MAIN GUARD
# ==========================================
if __name__ == "__main__":
    run_cricket_clustering_pipeline()