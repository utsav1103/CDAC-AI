import pandas as pd
import numpy as np

"""
Important parameters
Code	                    Meaning
df.dropna()	                Remove rows containing NaN
df.dropna(axis=1)	        Remove columns containing NaN
df.dropna(inplace=True)	    Modify original DataFrame
df.dropna(how="all")	    Remove rows where every value is missing
df.dropna(subset=["Age"])	Remove rows where Age is missing
"""

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Karan"],
    "Age": [22, np.nan, 23, 25, np.nan],
    "Marks": [75, 80, np.nan, 90, 85],
    "Salary": [30000, 35000, 40000, np.nan, 45000]
}

df = pd.DataFrame(data)

print(df)
print("*" * 60)
print(df.isnull())
print("*" * 60)
print(df.isna())
print("*" * 60)
print(df.isnull().sum())
print("*" * 60)
print(df.isnull().sum().sum())
print("*" * 60)
print(df[df.isnull().any(axis=1)])
print("*" * 60)
new_df = df.dropna()

print(new_df)
print("*" * 60)
new_df = df.dropna(axis=1)

print(new_df)
print("*" * 60)
df["Age"] = df["Age"].fillna(0)

print(df)
print("*" * 60)
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)
print("*" * 60)
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
print(df)
print("*" * 60)
print("*" * 60)