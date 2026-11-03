import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Karan", "Arjun", "Riya"],
    "Department": ["AI", "IT", "AI", "IT", "AI", "IT", "AI"],
    "Marks": [75, 80, 65, 90, 85, 70, 95],
    "Age": [22, 24, 23, 25, 21, 22, 24]
}

df = pd.DataFrame(data)

print(df.groupby("Department", as_index=False)["Marks"].mean())
print(df.groupby("Department")["Marks"].max())
print(df.groupby("Department")["Name"].count())
result = df.groupby("Department")["Marks"].agg(["mean","max","count","min"])
print(result)

print(df.sort_values("Marks", ascending=False))
print(df.groupby("Department")["Age"].mean())