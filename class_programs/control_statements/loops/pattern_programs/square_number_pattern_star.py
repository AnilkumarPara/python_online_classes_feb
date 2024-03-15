# WAP to print the squared number pattern
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
rows = int(input("Enter number of rows for the * square pattern: "))
cols = int(input("Enter number of columns for the * square pattern: "))
if rows == cols:
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            print('*', end=' ')
        print()
else:
    print("Number of rows and columns should same for the square patter, please re-enter the again")
