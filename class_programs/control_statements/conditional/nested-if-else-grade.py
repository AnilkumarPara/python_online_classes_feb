# WAP to find the grade of a student
percentage_of_marks = float(input("Enter the percentage of marks scored in the exam"))
if percentage_of_marks >= 70 and percentage_of_marks <=100:
    print("Student passed in the Distinction")
else:
    if percentage_of_marks >= 60 and percentage_of_marks <70:
        print("Student passed in the First class")
    else:
        if percentage_of_marks >= 50 and percentage_of_marks <60:
            print("Student passed in the Second class")
        else:
            if percentage_of_marks >= 35 and percentage_of_marks <50:
                print("Student passed in the Third class")
            else:
                if percentage_of_marks >= 0 and percentage_of_marks <35:
                    print("Student failed perfectly")
                else:
                    print("Student has entered the incorrect percentage of marks")
print("End of the program")
