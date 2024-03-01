# WAP for the car washing and user can choose the person
# Sequential Statements

# person = input("Enter the person name: ")
# print(person, "will clean the car")
# print("Car cleaning started")
# print("Car cleaning is in progress")
# print("Car cleaning completed")

# Control statements
no_of_cars = int(input("Enter the number of cars in the apartment: "))
i = 1
while i <= no_of_cars:
    car_cleaning_status = input(f"Enter 'Yes' if car-{i} is in cleaned state 'No' otherwise")
    if car_cleaning_status == 'No':
        person = input("Enter the person name: ")
        print(person, f"will clean the car-{i}")
        print(f"Car-{i} cleaning started")
        print(f"Car-{i} cleaning is in progress")
        print(f"Car-{i} cleaning completed")
    else:
        print(f"Car-{i} is already in the cleaned state")
    i = i+1
