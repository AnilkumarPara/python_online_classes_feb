# WAP to find the greatest of 3 numbers
a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
if a > b:
    if a > c:
        print("a is greater")
if b > a:
    if b > c:
        print("b is greater")
if c > a:
    if c > b:
        print("c is greater")
