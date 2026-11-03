import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Rahul", "Neha", "Karan"],
    "Age": [22.0, 24.0, 23.0, 22.0, 25.0, 21.0],
    "City": ["Delhi", "Bombay", "Mumbai", "Delhi", "Bombay", "Delhi"],
    "Marks": [75, 80, 65, 75, 90, 85]
}

df = pd.DataFrame(data)

print(df.duplicated())
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
df["City"] = df["City"].replace("Bombay","Mumbai")
#Convert the Age column from float to integer
df["Age"] = df["Age"].astype(int)
df.reset_index(drop=True, inplace=True)
print(df)