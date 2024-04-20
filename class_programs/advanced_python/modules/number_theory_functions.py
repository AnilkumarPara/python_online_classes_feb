def prime_number(n):
    """
    This function checks given number is Prime or not
    :param n: Can input any integer value
    :return: True or False or String for negative numbers, 0, 1
    """
    if n > 1:
        counter = 0
        for i in range(1, n + 1):
            if n % i == 0:
                counter += 1
        if counter == 2:
            return True
        else:
            return False
    else:
        return "Prime numbers apply only to Positive numbers greater than 1."


def factorial_of_number(n):
    """
    This function calculates the factorial for non-negative numbers
    :param n: Can input any integer value
    :return: Positive integer or String for negative numbers
    """
    result = 1
    num = n
    if n >= 0:
        if n == 0:
            print(f"factorial of {num} =", result)
        else:
            while n >= 1:
                result = result * n
                n = n - 1
            return result
    else:
        return "The factorial function is only defined for non-negative integers"


def palindrome_number(n):
    num = n
    reversed_num = 0
    while n > 0:
        reminder = n % 10
        reversed_num = reversed_num * 10 + reminder
        n = n // 10
    if num == reversed_num:
        return True
    else:
        return False


def add(a, b, c):
    return a+ b + c