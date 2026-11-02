import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Karan"],
    "Age": [22, 24, 23, 25, 21],
    "Marks": [75, 80, 65, 90, 85]
}

df = pd.DataFrame(data)
print(df.head(3))
print(df.shape)
print(df.columns)
print(df["Marks"])
print(df[["Name","Marks"]])

