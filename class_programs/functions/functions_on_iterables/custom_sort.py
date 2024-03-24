people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 35},
]

# Sort the list of people based on their ages (custom key function)
people.sort(key=lambda x: x["age"])

# Print the sorted list
for person in people:
    print(f"{person['name']} ({person['age']} years old)")

# Outputs:
# Charlie (20 years old)
# Alice (25 years old)
# Bob (30 years old)
# David (35 years old)
