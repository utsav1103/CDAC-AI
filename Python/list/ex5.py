num = [5, 10, 15, 20, 25, 5, 21, 5, 30, 5]
duplicate = []

# print(num.count(5))

for n in num:
    if n not in duplicate: # this will add the number to the duplicate and will ignore the next time it comes in the list
        duplicate.append(n)
print(duplicate)