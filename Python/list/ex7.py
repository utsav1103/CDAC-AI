def main():
    numbers = []
    for i in range(5):
        num = int(input("Enter a number:"))
        numbers.append(num)

    print("List :", numbers)
    print("Maximum :", max(numbers))
    print("Minimum :", min(numbers))
    print("Sum :", sum(numbers))
    print("Average :", sum(numbers)/len(numbers))

main()