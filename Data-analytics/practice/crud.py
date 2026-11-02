import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Karan"],
    "Age": [22, 24, 23, 25, 21],
    "Marks": [75, 80, 65, 90, 85]
}

df = pd.DataFrame(data)

print(df)

df["City"] = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
print(df)

df["Bonus_Marks"] = df["Marks"] + 5
print(df)

new_student = {
    "Name": "Arjun",
    "Age": 23,
    "Marks": 88,
    "City": "Bhopal",
    "Bonus_Marks": 93
}

df.loc[len(df)] = new_student

print(df)