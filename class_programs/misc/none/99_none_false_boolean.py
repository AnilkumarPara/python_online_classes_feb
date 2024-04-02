# Example showing None in a Boolean context

my_var = None

# Checking my_var in a Boolean context
if my_var:
    print("my_var is True")
else:
    print("my_var is False")  # This will be executed

# Checking my_var's identity and equality
if my_var is None:
    print("my_var is None")  # This will be executed

if my_var == False:
    print("my_var is False")
else:
    print("my_var is not False")  # This will be executed

if my_var == 0:
    print("my_var is 0")
else:
    print("my_var is not 0")  # This will be executed

if my_var == "":
    print("my_var is an empty string")
else:
    print("my_var is not an empty string")  # This will be executed
