def calculate(a, b):
    print("Division:", a / b)
    print("Remainder:", a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b != 0:
    calculate(a, b)
else:
    print("Division by zero is not possible")