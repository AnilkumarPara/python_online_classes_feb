def palindrome(n):
    """
    This function checks if given number is palindrome or not
    If yes, prints number is a palindrome number
    If no, prints number is not a palindrome number
    :param n:
    :return: None
    """
    num = n
    reversed_num = 0
    while n > 0:
        reminder = n % 10
        reversed_num = reversed_num*10 + reminder
        n = n//10
    if num == reversed_num:
        print(num, "is a palindrome number")
    else:
        print(num, "is not a palindrome number")






