def main():

    num = int(input("Enter a number: "))
    

    if num <= 0:
        print("Please enter a positive integer.")

    else:
        a = 0
        b = 1

        print("Fibonacci sequence:")
        for i in range(num):
            print(a, end=" ")
            c = a+b
            a = b
            b = c
    


main()    