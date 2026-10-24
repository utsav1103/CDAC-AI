def main():
    numbers = []

    for i in range(5):
        num = int(input("Enter a number:"))
        numbers.append(num)

    print("List :",numbers)
    even_num = []

    for i in numbers:
        if i % 2 == 0:
            even_num.append(i)
    print("Even numbers :", even_num)
    print("Count of even num:",len(even_num))

main()