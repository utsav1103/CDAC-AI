import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha"],
    "Age": [22, 24, 23, 25],
    "Marks": [75, 80, 45, 90]
}

df = pd.DataFrame(data)
df["Department"] = ["IT", "HR", "IT", "AI"]
new_student = {
    "Name": "Karan",
    "Age": 21,
    "Marks": 85,
    "Department": "AI"
}

df.loc[len(df)] = new_student

df.loc[df["Name"] == "Rahul", "Marks"] = 95

df.drop("Age", axis=1,inplace=True)

df.drop(df[df["Marks"] < 50].index, inplace=True)

print(df)