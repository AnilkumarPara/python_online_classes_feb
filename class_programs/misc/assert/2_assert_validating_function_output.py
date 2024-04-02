# Example 2: Validating Function Output
# You can also use assert to validate the output of a function.

def get_age_category(age):
    if 0 <= age < 18:
        return "child"
    elif 18 <= age < 60:
        return "adult"
    elif 60 <= age <= 150:
        return "senior citizen"
    else:
        return "User entered the Invalid age"


person_age = int(input("Enter person's age: "))
category = get_age_category(person_age)
print(category)
assert category in ["child", "adult", "senior citizen"], "Invalid age category"
