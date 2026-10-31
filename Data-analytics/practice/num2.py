import numpy as np

marks = np.array([35, 45, 60, 75, 90])

#np.where(condition, value_if_true, value_if_false)

result = np.where(marks >= 50, "Pass", "Fail")

print(result)

salary = np.array([30000, 45000, 70000])

adjusted = np.where(salary < 50000, salary + 5000, salary)

print(adjusted)

#NumPy statistical operations

print(np.sum(marks))
print(np.mean(marks))
print(np.median(marks))
print(np.min(marks))
print(np.max(marks))
print(np.std(marks))
print(np.var(marks))