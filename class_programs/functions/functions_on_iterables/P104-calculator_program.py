# Global Variable
calculation_history = []


def add(x, y):
    result = x + y  # Local Variable
    calculation_history.append(f"{x} + {y} = {result}")
    return result


def display_history():
    for entry in calculation_history:
        print(entry)


# Usage
print(add(10, 20))
print(add(5, 7))
display_history()
