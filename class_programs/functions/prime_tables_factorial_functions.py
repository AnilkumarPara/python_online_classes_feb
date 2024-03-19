def generate_prime_numbers(n):
    """
    This function generates prime numbers from 2 to n
    :param n: Can input any integer value
    :return: None
    """
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


def multiplication_table(n):
    """

    :param n: Can input any integer value
    :return: None
    """
    for number in range(1, n + 1):
        print("Multiplication table for ", number)
        for i in range(1, 11):
            print(number, '*', i, '=', number * i)
        print()


def factorial(n):
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


# generate_prime_numbers(5)
