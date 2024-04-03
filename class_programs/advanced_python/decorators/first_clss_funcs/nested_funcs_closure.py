# nested function
# A function inside a function is called the nested function

def outer_func(message):
    print(message)
    print("outer function")

    def inner_func():
        print("inner function")
        print(message)
    return inner_func


inner = outer_func("Hello")
inner()
