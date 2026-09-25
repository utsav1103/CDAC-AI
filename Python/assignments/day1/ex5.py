def main():

    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    opp = input("Enter operator (+, -, *, /):")

    if opp == '+':
        print(num1, "+", num2, "=", num1 + num2)
    elif opp == '-':
        print(num1, "-", num2, "=", num1 - num2)
    elif opp == '*':
        print(num1, "*", num2, "=", num1 * num2)
    elif opp == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(num1, "/", num2, "=", num1 / num2)            
    else:
        print("Invalid operator. Please enter one of +, -, *, /.")

main()    