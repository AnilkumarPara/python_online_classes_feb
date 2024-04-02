import math

# Without function as argument
print("-- Without function as argument --")


def calc_square_root(list_var):
    result = []
    for num in list_var:
        result.append(num ** 0.5)
    return result


print(calc_square_root([1, 2, 3, 4]))


def calc_square(list_var):
    result = []
    for num in list_var:
        result.append(num ** 2)
    return result


print(calc_square([1, 2, 3, 4]))


def calc_cube(list_var):
    result = []
    for num in list_var:
        result.append(num ** 3)
    return result


print(calc_cube([1, 2, 3, 4]))


def calc_log10(list_var):
    result = []
    for num in list_var:
        result.append(math.log10(num))
    return result


print(calc_log10([1, 2, 3, 4]))

# With function as argument
print()
print("-- With function as argument --")


def square_root(n):
    return n ** 0.5


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def log10_calculator(number):
    return math.log10(number)


def my_map(func, list_var):
    print(func.__name__)
    result = []
    for num in list_var:
        result.append(func(num))
    return result


print(my_map(square_root, [1, 2, 3, 4]))
print(my_map(square, [1, 2, 3, 4]))
print(my_map(cube, [1, 2, 3, 4]))
print(my_map(log10_calculator, [1, 2, 3, 4]))
