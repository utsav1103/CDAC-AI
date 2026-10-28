# import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60])

# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)

import numpy as np

# a = np.array([10, 20, 30, 40])
# b = np.array([1, 2, 3, 4])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

#* Broadcasting
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

print(a + b)

print(a + 5)

#boolean operations

marks = np.array([35, 45, 60, 75, 90])

print(marks < 50)
print(marks >= 60)
print(marks == 45)
print(marks != 75)

# masking boolean

result = marks > 50
print(marks[result])


# multiple conditions

result1 = marks[(marks >= 50) & (marks <= 80)]

print(result1)