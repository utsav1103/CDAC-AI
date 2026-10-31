
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Generate the dataset
n_samples = 200
np.random.seed(2026)

fertilizer = np.random.uniform(20, 250, size=n_samples)

true_yield = (
    2.0
    + 0.08 * fertilizer
    - 0.00028 * (fertilizer ** 2)
)

observed_yield = true_yield + np.random.normal(
    0, 0.8, size=n_samples
)

df = pd.DataFrame({
    "fertilizer_kg_ha": fertilizer.round(1),
    "crop_yield_tons": observed_yield.round(2)
})

print("Dataset preview:")
print(df.head())

# 2. Separate input (X) and output (y)
X = df[["fertilizer_kg_ha"]]
y = df["crop_yield_tons"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create a Polynomial Regression model
model = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),
    LinearRegression()
)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Squared Error:", round(mse, 4))
print("R2 Score:", round(r2, 4))

# 7. Predict yield for new farm plots
new_farm_plots = pd.DataFrame({
    "fertilizer_kg_ha": [50.0, 140.0, 220.0]
})

predictions = model.predict(new_farm_plots)

# 8. Display predictions
results = new_farm_plots.copy()
results["predicted_yield_tons"] = predictions.round(2)

print("\nPredictions for new farm plots:")
print(results)
