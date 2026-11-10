# Task 4: Bank Account


class BankAccount:
    """A bank account with an owner and a balance."""

    def __init__(self, owner, balance=0):
        """Store the owner and starting balance on the object."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Take money out, or refuse if there is not enough."""
        if amount > self.balance:
            print(f"Withdrawal of £{amount:.2f} refused - not enough money.")
            return False
        self.balance -= amount
        return True

    def show_balance(self):
        """Print the current balance."""
        print(f"{self.owner}'s balance: £{self.balance:.2f}")


account = BankAccount("Mahin")
account.show_balance()
account.deposit(100)
account.deposit(50)
account.show_balance()
account.withdraw(30)
account.show_balance()
account.withdraw(500)        # should fail
account.show_balance()
