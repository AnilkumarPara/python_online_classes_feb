# Example 1: Checking Function Arguments

"""
Assert statements are often used to check the
validity of arguments passed to a function.
"""


def prime_number(n):
    """
    This function checks given number is Prime or not
    :param n: Can input any integer value
    :return: string
    """
    assert n > 1, "Prime numbers apply only to Positive numbers greater than 1."
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    if counter == 2:
        return "Given number is a Prime Number"
    else:
        return "Given number is not a Prime Number"


# print(prime_number(4))  # No issue, prints Given number is not a Prime Number
# print(prime_number(7))  # No issue, prints Given number is a Prime Number
print(prime_number(0))  # AssertionError: Prime numbers apply only to Positive numbers greater than 1.
