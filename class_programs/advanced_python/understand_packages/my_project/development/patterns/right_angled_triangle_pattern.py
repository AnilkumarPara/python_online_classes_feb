def right_angled_triangle_pattern(n):
    """
    prints the Right-Angled Triangle Number Pattern for given n
    :param n:
    :return: None
    """
    for row in range(1, n+1):
        for col in range(1, row + 1):
            print(col, end=" ")
        if row != n:
            print()
