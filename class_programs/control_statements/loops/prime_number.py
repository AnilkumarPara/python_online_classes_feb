n = int(input("Enter a number to find the given number is Prime or not: "))
i = 2

if n == 1:
    print(f"{n} is not a prime number")
elif n >= 2:
    while i < n:
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
        i = i + 1
    else:
        print(f"{n} is a prime number")
else:
    print("Prime number is applied to only positive numbers")
