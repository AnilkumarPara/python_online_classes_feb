def welcome_greetings():
    print("Welcome to the party")


def thanks_greetings():
    print("Thanks for attending the party")


funcs = [welcome_greetings, thanks_greetings]
for fun in funcs:
    fun()
