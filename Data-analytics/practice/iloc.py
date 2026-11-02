#loc and iloc
#They are used to select rows and columns from a data frame based on labels and integer-based indexing respectively 
"""
Understanding loc
loc selects data using row labels and column names.

Let's use this DataFrame:
"""

import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Karan"],
    "Age": [22, 24, 23, 25, 21],
    "Marks": [75, 80, 65, 90, 85]
}

df = pd.DataFrame(data)
print(df.loc[0]) # Selects the first row using label-based indexing
print(df.loc[0, "Marks"]) # Selects the value in the first row and "Marks" column using label-based indexing
print(df.loc[0:2]) # Selects the first three rows using label-based indexing
#Important loc includes the ending label.
print(df.loc[:, ["Name", "Marks"]]) #: means all rows


""" Understanding iloc
iloc selects data using integer positions.

For example """

print(df.iloc[0])
print(df.iloc[0, 2])
print(df.iloc[0:3])
print(df[df["Marks"] > 75])
print(df[df["Age"] >= 23])
print(df[(df["Age"] >= 22) & (df["Marks"] >= 75)])

"""
Difference between loc and iloc
Feature	        loc	                iloc
Selection	    Labels	            Integer positions
Columns	        Column names	    Column positions
Ending slice	Included	        Excluded
Example	        df.loc[0, "Age"]	df.iloc[0, 1]

"""

print(df.loc[:,["Name","Marks"]])
print(df.iloc[0:3,0:2])
print(df[df["Marks"] >= 80])
print(df[(df["Age"] > 22) & (df["Marks"] > 70)])
