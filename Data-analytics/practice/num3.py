import numpy as np

marks = np.array([25,45,55,70,85])

print(marks[marks >= 55])

print(marks[(marks >= 40) & (marks <= 75)])

arr1 = np.array([[1,2,3],[4,5,6]]) 
arr2 = np.array([10,20,30])

print(arr1 + arr2)
