# Positional arguments/required arguments
def power(a, b):
    return a ** b


# print(power(3, 2))

def greet_message(greet, name):
    print(f"{greet} {name}")


# greet_message('Sachin', 'Hi')

# Keyword arguments

def student_data(name, roll_no, age, marks):
    print(f"Student {name} with roll_no {roll_no} , with age {age}, got {marks}")


# student_data(roll_no=18, age=19, marks=25,name='sachin')

# Default arguments
def increment(number, by=1):
    return number + by


# print(increment(5, 2))

# Variable length arguments
# *args
def add(*numbers):
    sum_values = 0
    for number in numbers:
        sum_values = sum_values + number
    print("addition=", sum_values)


# add(2, 3, 4)
# add(5,6,7,8,9)

# **kwargs
def introduce_yourself(*args, **kwargs):
    print(args)
    print(kwargs)



# introduce_yourself(name='Anil', age=35)
introduce_yourself('Anil',2000, age=35, designation='software engineer')
