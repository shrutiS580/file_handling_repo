# a = input("enter your first numbet: ")
# b = input("enter your second number: ")
try:
    a = input("enter your first numbet: ")
    b = input("enter your second number: ")
    a = int(a)
    b = int(b)
    div = a / b
    add = a +b 
    mul = a*b
    sub = a -b
    print("division", div)
    print("addition", add)
    print("multiplication", mul)
    print("substraction", sub)


except ZeroDivisionError:
    print("con not divided by zero")

except ValueError:
    print("enter a valid value")    

except Exception as e :
    print("error" , e)
finally :
    print("thank you")

