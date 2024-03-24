# Calculate the factorial of a number
n = int(input("Enter the number to calculate the factorial "))
result = 1
num = n
if n >= 0:
    if n == 0:
        print(f"factorial of {num} =", result)
    else:
        while n >= 1:
            result = result * n
            n = n - 1
        print(f"factorial of {num} =", result)
else:
    print("The factorial function is only defined for non-negative integers")
