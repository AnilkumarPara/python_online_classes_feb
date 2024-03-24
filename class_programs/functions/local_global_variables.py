a = 5  # global variable


def local_global():
    print("globals=", globals())
    print("Inside the function global a=", globals()['a'])
    globals()['a'] = 25
    print("Inside the function global a after update=", globals()['a'])
    a = 10  # local variable
    print("Inside a function before a=", a)
    a = 100
    print("Inside a function local after update a=", a)


local_global()
print("outside the function a=", a)
