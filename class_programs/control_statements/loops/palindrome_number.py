"""
A palindrome number is a number that remains the same when its digits are reversed.
For example, 121, 1331, 16461 are palindrome numbers, while 123 and 321 are not.
"""
n = int(input("enter a number"))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if temp == rev:
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
