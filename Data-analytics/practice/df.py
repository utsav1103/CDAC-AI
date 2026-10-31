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