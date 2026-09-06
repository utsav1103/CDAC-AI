numbers = [5, 10, 15, 20, 25]

print(numbers)

numbers.append(30)
print(numbers)

numbers.insert(2, 13)
print(numbers)

numbers.remove(15)
print(numbers)

numbers.pop()
print(numbers)

num2 = numbers.copy()
numbers.append(14)
print(numbers)
print(num2)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)