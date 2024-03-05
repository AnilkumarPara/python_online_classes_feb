# WAP to find the greatest of 3 numbers
a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
if a > b and a > c:
    print("a is greater")
if b > a and b > c:
    print("b is greater")
if c > a and c > b:
    print("c is greater")
