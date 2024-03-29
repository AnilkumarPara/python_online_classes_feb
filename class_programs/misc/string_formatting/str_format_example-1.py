# You want to greet someone
name = input("Enter the name to greet: ")
# Hello Anil
# print("Hello", name)

# You want to add 2 numbers and print on the screen
# Addition = 6
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Old Style (%-formatting)
print("--- Old Style (%-formatting)  ---")
print("Hello %s" % name)
print("Addition = %d" % (a + b))

# str.format() Method
print("--- Using format() method  ---")
print("Hello {}".format(name))
print("Addition = {}".format(a+b))

# Using f-string (Formatted String Literals)
print("--- Using f-string  ---")
print(f"Hello {name}")
print(f"Addition = {a+b}")
