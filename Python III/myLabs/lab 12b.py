"""
When you compare for equality, the default version of __eq__ is called automatically
    This will blindly compare two instances which will never be equal
To override this result, implement one or more of the newer magic methods, in our case __eq__
    Use this magic method to compare the balances of the two accounts
    Test by using equal and non-equal balances
Pay attention to which instance is passed to self.
Change the balances to test both possible outcomes
"""


class BankAccount:  # Top tier class (super class) in Python 2 or 3
    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable

    def __str__(self):
        return f"Account: {self.acctname}\tBalance: ${self.balance}"

    def __eq__(self, other):
        return self.balance == other.balance

    def deposit(self, amount):     # another method
        if amount < 0:
            return 4   # Negative deposits are really withdrawals
        self.balance += amount
        return 0        # Deposit successful

    def get_balance(self):
        return self.balance

    def print_balance(self):
        print(f"Balance for {self.acctname}: ${self.get_balance()}")

    def withdrawal(self, amount):
        if amount < 0:
            return 4

        elif self.balance - amount < 0:
            return 4

        else:
            print(f"Current Balance: ${self.get_balance()}\t Withdrawal Amount: ${amount}")
            self.balance -= amount
            print(f"New Balance for {self.acctname}: ${self.get_balance()}")
            return 0


def main():
    a = BankAccount('Monty Python')  # Create an instance of Bankaccount
    b = BankAccount('Guido van Rossum')  # Create another instance

    ret_code = a.deposit(500) # Deposit $100 into account a
    if ret_code > 0:
        print('Deposit failed')  # Return > 0

    ret_code = b.deposit(500) # Deposit $500 into account b
    if ret_code > 0:
        print('Deposit failed')  # Return > 0

    if a == b:
        print("They're equal!")
    else:
        print("Not equal!")

    a.print_balance()
    b.print_balance()


if __name__ == '__main__':
    main()