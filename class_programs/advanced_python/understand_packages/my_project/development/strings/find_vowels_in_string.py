def count_display_vowels(string):
    """
    This function Counts and display vowels in a given string
    :param string:
    :return: None
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counter = 0
    for char in string:
        if char in vowels:
            print(char)
            counter += 1
    print("Total Number of vowels in a string =", counter)




