print("Start")


def decorator_func(original_function):
    def wrapper_func():
        print("Executing wrapper function", wrapper_func.__name__)
        original_function()

    return wrapper_func


@decorator_func
def display():
    print("Executing display function")


display()


@decorator_func
def display_info():
    print("display_info")


display_info()
