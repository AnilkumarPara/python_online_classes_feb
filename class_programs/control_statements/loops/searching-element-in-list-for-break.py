# Searching for an Element in a List using for and break

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = int(input("Enter a element to search from a list: "))
counter = 0
for number in numbers:
    if number == search_element:
        counter = counter + 1
        break
if counter == 1:
    print("Search element is found")
else:
    print("Search element is not found")

print("End of the program")















