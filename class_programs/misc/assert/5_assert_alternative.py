# Scenario 2: Handling Runtime Errors in Production Code
"""
For production code, you should handle potential errors gracefully
using try-except blocks or conditional statements,
rather than relying on assert statements.
"""


def calculate_discount(price, discount):
    # Handling invalid discount rate with an exception
    if not 0 <= discount <= 1:
        raise ValueError("Discount rate must be between 0 and 1")
    return price * (1 - discount)


try:
    # This will catch the ValueError and handle it gracefully
    final_price = calculate_discount(100, 1.5)
except ValueError as e:
    print(f"Error: {e}")
