# 1. Function without arguments and no return value

def greetings():
    print("Hello")


greetings()


# 2. Function with arguments and no return value
def greeting_message(name):
    print(f"Hello {name}")


greeting_message('Anil')


# 3. Function with arguments and with return value
def add(a, b):
    addition = a + b
    return addition


sum_of_values = add(2, 3)
print(sum_of_values)


# 4. Function without arguments and return value

def retrieve_pi_value():
    return 3.14


pi = retrieve_pi_value()
print(pi)
