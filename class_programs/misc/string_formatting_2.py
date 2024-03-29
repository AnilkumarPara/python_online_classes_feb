# My name is Anil and I am 37 years old
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Old Style (%-formatting)
print("--- Old Style (%-formatting)---")
print("My name is %s and I am %d years old" % (name, age))

# str.format() Method
print("--- format() Method ---")
print("My name is {} and I am {} years old".format(name, age))

# Using f-string (Formatted String Literals)
print("--- Formatted String Literals (f-strings) ---")
print(f"My name is {name} and I am {age} years old")
