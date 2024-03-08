"""
WAP to find the grade of all students in class based on the percentage of marks
student scored in the exam using while and if elif ladder
"""
total_no_of_students = int(input("Enter the number of students in a class: "))
i = 1
while i <= total_no_of_students:
    percentage_of_marks = float(input(f"Enter the percentage of marks student-{i} secured in the exams: "))
    if 90 <= percentage_of_marks <= 100:
        print(f"student-{i} has passed in the A1 Grade")
    elif 80 <= percentage_of_marks < 90:
        print(f"student-{i} has passed in the A2 Grade")
    elif 70 <= percentage_of_marks < 80:
        print(f"student-{i} has passed in the B1 Grade")
    elif 60 <= percentage_of_marks < 70:
        print(f"student-{i} has passed in the B2 Grade")
    elif 50 <= percentage_of_marks < 60:
        print(f"student-{i} has passed in the C1 Grade")
    elif 40 <= percentage_of_marks < 50:
        print(f"student-{i} has passed in the C2 Grade")
    elif 33 <= percentage_of_marks < 40:
        print(f"student-{i} has passed in the D Grade")
    elif 0 <= percentage_of_marks < 33:
        print(f"student-{i} failed in the exam, Grade is E")
    else:
        print(f"student-{i} has entered the incorrect marks, please re-enter the correct marks")
    i = i + 1
print("End of the program")

