import math

print(10/3)
print(10//3)
print(10%3)
print(10**3)


x = 10
x += 5
print(x)


x = 10
x -= 5
print(x)

# ? parentheses > exponential operator > multiplication > division > addition > subtraction
x = (10 + 3) * 2 ** 2
print(x)

#* math functions

x = 2.9
print(round(x))

x = -2.9
print(abs(x))

x = 3.6
print(math.ceil(x))  # rounds up to the nearest integer
print(math.floor(x))  # rounds down to the nearest integer