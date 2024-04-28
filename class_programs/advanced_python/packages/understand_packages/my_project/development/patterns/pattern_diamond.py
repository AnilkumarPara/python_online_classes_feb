def diamond_pattern(n):
    """
    prints the diamond pattern for given n
    :param n:
    :return: None
    """
    for row1 in range(1, n+1):
        print(' '*(n-row1) + '*'*((2*row1)-1))
    for row2 in range(1, n):
        print(' '*row2 + '*'*((2*(n-row2))-1))

