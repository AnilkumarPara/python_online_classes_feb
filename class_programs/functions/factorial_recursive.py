def factorial(num):
    if num >= 0:
        # base case
        if num == 0 or num == 1:
            return 1
        # recursive case
        else:
            return num * factorial(num - 1)
    else:
        return "Factorial can't be calculated for the negative numbers"


n = int(input("Enter a number to find the factorial: "))
print(factorial(n))
