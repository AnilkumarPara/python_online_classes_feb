# WAP to print the Right Angled Triangle pattern
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

rows = int(input("Enter number of rows for the Right Angled Triangle pattern: "))
for row in range(rows, 0, -1):
    for col in range(1, row+1):
        print(col, end=' ')
    print()
