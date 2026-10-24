def calculate_average(numbers):
    if not numbers:
        return 0
    else:
        result = sum(numbers) / len(numbers)
    return result
print(calculate_average((10,20,30)))


