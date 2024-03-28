"""
Creating a dictionary of squares for numbers from 1 to 5
using dictionary comprehension
"""
numbers = [1, 2, 3, 4, 5]
print({number:number * number for number in numbers})
