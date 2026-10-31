#A DataFrame is a two-dimensional 
# labeled data structure.

#Think of it as an Excel spreadsheet 
# containing rows and columns.
import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha"],
    "Age": [22, 24, 23, 25],
    "Marks": [75, 80, 65, 90]
}

df = pd.DataFrame(data)

print(df)
"""
Command	        Purpose
df.head()	    First 5 rows
df.tail()	    Last 5 rows
df.shape	    Number of rows and columns
df.columns	    Column names
df.index	    Row indexes
df.dtypes	    Data types of columns
df.info()	    Dataset structure and non-null counts
df.describe()	Statistical summary
df.size	        Total number of elements
"""

print(df.head(2))
print("*"*10)
print(df.shape)
print("*"*10)
df.info()
print("*"*10)
print(df.describe())

#Selecting columns
print(df["Name"])

#Select multiple columns
print(df[["Name", "Marks"]])