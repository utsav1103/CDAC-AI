import numpy as np
import pandas as pd

marks = pd.Series([75, 80, 65, 90, 85])

print(marks)

#You can also create your own index

mark = pd.Series(
    [75, 80, 65],
    index=["Rahul", "Aman", "Priya"]
)
print(mark)
print(mark["Rahul"])