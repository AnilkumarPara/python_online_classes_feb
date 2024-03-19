def student_data(name,roll_no,age,marks):
    print(f"Student {name} with roll_no {roll_no} , with age {age}, got {marks}")

student_data(roll_no=18,age=19,marks=25,name='sachin')

n = int(input("Enter a number, to find prime numbers from 2 to n: "))
if n > 1:
    for number in range(2, n + 1):
        counter = 0
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter == 2:
            print(number)
else:
    print("Prime numbers apply only to Positive numbers greater than 1.")


