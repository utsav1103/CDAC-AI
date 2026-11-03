import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha"],
    "City": ["Delhi", "Bombay", "Delhi", "Bombay"],
    "Marks": [75, 80, 65, 90]
}

df = pd.DataFrame(data)

df["City"] = df["City"].replace("Bombay","Mumbai")
print(df)
df["City"] = df["City"].replace({
    "Delhi": "New Delhi",
    "Mumbai": "Mumbai City"
})
print(df)
print(df.dtypes)