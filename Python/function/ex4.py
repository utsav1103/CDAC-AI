def calculate(a,b=10):
    return a+b,a-b,a*b
sum , sub , mul = calculate(10,5)

print("Sum:",sum)
print("Subtraction:",sub)
print("Product:",mul)

addition, difference,multiplication = calculate(20)

print("Addition:",addition)
print("Difference:",difference)
print("Multiplication:",multiplication)