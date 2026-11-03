import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Rahul", "Neha"],
    "Age": [22, 24, 23, 22, 25],
    "Marks": [75, 80, 65, 75, 90]
}

df = pd.DataFrame(data)

print(df)
print(df.duplicated())
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)
print(df)