"""
Creating a dictionary of squares for numbers from 1 to 5
using dictionary comprehension
"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = {}
for number in numbers:
    squared_numbers.setdefault(number, number*number)
print(squared_numbers)
