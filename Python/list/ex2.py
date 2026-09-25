#? write a program to find the largest number  in a list

def main():

    numbers = [10, 20, 30, 40, 50 , 114 , 38 , 46, 76]
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print("The largest number in the list is:", largest)

main()    