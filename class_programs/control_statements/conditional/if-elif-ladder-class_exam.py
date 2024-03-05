# WAP to find the class of a student passed in the exam based on percentage
percentage_of_marks = float(input("Enter the percentage of marks scored in the exam"))
if 70 <= percentage_of_marks <= 100:
    print("Student passed in the Distinction")
elif 60 <= percentage_of_marks < 70:
    print("Student passed in the First class")
elif 50 <= percentage_of_marks < 60:
    print("Student passed in the Second class")
elif 35 <= percentage_of_marks < 50:
    print("Student passed in the Third class")
elif 0 <= percentage_of_marks < 35:
    print("Student failed successfully")
else:
    print("Student has entered the incorrect marks, please re-enter again")
print("End of the program")
