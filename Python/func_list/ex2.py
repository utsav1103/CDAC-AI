def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

values = [3,5,2,24,8,1,47]
result = count_even(values)
print("The count of even numbers is:",result)