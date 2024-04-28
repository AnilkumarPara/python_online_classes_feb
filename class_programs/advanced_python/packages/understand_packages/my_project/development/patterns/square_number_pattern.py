def sequential_square_number_pattern(n):
    """
    It prints Row-Repeated Sequential Square Number Pattern for given number
    :param n:
    :return: None
    """
    for row in range(1, n+1):
        for col in range(1, n+1):
            print(col, end=' ')
        if row != n:
            print()

















"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
