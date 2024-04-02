# Scenario 1: Using assert in Development (Debugging Tool)
"""
In this example, an assert statement is used to check
a condition during the development phase. It's helpful for catching
bugs early but is not intended for error handling in production.
"""


def calculate_discount(price, discount):
    # Assert statement to ensure discount rate is reasonable during development
    assert 0 <= discount <= 1, "Discount rate must be between 0 and 1"
    return price * (1 - discount)


# This will raise an AssertionError if the discount is not within the expected range
calculate_discount(100, 1.5)  # This is okay during development for debugging
