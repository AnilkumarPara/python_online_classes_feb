class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")


# Creating accounts for two people
alice_account = BankAccount("Alice")
bob_account = BankAccount("Bob")

# Alice and Bob performing transactions
alice_account.deposit(100)
alice_account.withdraw(30)

bob_account.deposit(200)
bob_account.withdraw(50)
