n = int(input("Enter a number, to find prime numbers from 2 to n: "))
if n > 1:
    for number in range(2, n + 1):
        counter = 0
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter == 2:
            print(number)
else:
    print("Prime numbers apply only to Positive numbers greater than 1.")

num = int(input("Enter a number to print the multiplication table for given number: "))
for number in range(1, num + 1):
    print("Multiplication table for ", number)
    for i in range(1, 11):
        print(number, '*', i, '=', number * i)
    print()

n = int(input("Enter a number to find factorial of a given number: "))
result = 1
num = n
if n >= 0:
    if n == 0:
        print(f"factorial of {num} =", result)
    else:
        while n >= 1:
            result = result * n
            n = n - 1
        print("factorial of a number is ", result)
else:
    print("The factorial function is only defined for non-negative integers")
