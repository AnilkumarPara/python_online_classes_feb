# nested if
"""
WAP to get the Karachi biscuits, when your friend goes to Hyderabad, Ameerpet,
Karachi biscuits shop
"""
city_name = input("Enter city name: ")
if city_name == 'Hyderabad':
    area_name = input("Enter area name: ")
    if area_name == 'Ameerpet':
        shop_name = input("Enter shop name: ")
        if shop_name == 'Karachi':
            print("Get the biscuits")
print("End of the program")
