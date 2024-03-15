# WAP to print the following pyramid pattern
n = 7
"""
   *
  ***
 *****
*******
"""
for row in range(1, n+1):
    print(" " * (n - row) + "*" * ((2 * row)-1))
