import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Karan", "Arjun"],
    "Department": ["AI", "IT", "AI", "IT", "AI", "IT"],
    "Marks": [75, 80, 65, 90, 85, 70],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Male"],
    "Age": [22, 24, 23, 25, 21, 22]
}

df = pd.DataFrame(data)

# print(df)
print(df.groupby("Department")["Marks"].mean())
print(df.groupby("Department")["Marks"].sum())
print(df.groupby("Department")["Marks"].max())
print(df.groupby("Department")["Marks"].min())
print(df.groupby("Department")["Marks"].count())
print(df.groupby("Department")["Marks"].std())

# Multiple aggregations using agg()
result = df.groupby("Department")["Marks"].agg(["mean", "sum","max","min","count","std"])
print(result)

print(df.groupby(["Department", "Gender"])["Marks"].mean())

print(df.sort_values("Marks"))
print(df.sort_values("Marks", ascending=False))

print(df.sort_values(
    ["Department", "Marks"],
    ascending=[True, False]
))