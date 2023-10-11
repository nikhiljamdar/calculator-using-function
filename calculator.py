a = int(input("Enter a first number :"))
b = int(input("Enter a second number :"))
choice = input("Enter your choice {+,-,*,/} :")
def add(a,b):
    c = a+b
    return c
def sub(a,b):
    c = a-b
    return c
def mult(a,b):
    c = a*b
    return c
def div(a,b):
    c = a/b
    return c

if choice == "+":
    print(add(a,b))
elif choice == "-":
    print(sub(a,b))
elif choice == "*":
    print(mult(a,b))
elif choice == "/":
    print(div(a,b))
else:
    print("Invalid Input")




