def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Insufficient funds.")
        return balance


# Initial balances
alice_balance = 0
bob_balance = 0

# Alice and Bob performing transactions
alice_balance = deposit(alice_balance, 100)
alice_balance = withdraw(alice_balance, 30)
print(f"Alice's final balance is {alice_balance}.")

bob_balance = deposit(bob_balance, 200)
bob_balance = withdraw(bob_balance, 50)
print(f"Bob's final balance is {bob_balance}.")
