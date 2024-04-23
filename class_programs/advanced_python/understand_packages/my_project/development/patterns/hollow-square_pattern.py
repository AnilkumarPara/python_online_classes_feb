def hollow_square_star_pattern(n):
    """
    prints the hollow square star pattern for given n
    :param n:
    :return: None
    """
    for row in range(1, n+1):
        for col in range(1, n+1):
            if row == 1 or col == 1 or row == n or col == n:
                print('*', end=' ')
            else:
                print(" ", end=" ")
        print()


