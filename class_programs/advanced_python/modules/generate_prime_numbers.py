# Find all prime numbers between 2 and n
from number_theory_functions import prime_number

n = int(input("Enter a 'n' value to find the prime numbers from '2 to n' "))
if n > 1:
    for number in range(2, n+1):
        if prime_number(number):
            print(number)
else:
    print("Prime numbers apply only to natural numbers greater than 1.")
