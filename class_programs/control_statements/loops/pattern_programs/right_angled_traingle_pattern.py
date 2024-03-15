# WAP to print the Right Angled Triangle pattern
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

rows = int(input("Enter number of rows for the Right Angled Triangle pattern: "))
for row in range(1, rows+1):
    for col in range(1, row+1):
        print(col, end=' ')
    print()
