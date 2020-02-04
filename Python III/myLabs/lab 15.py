"""
Change the previous program to allow, in addition to the normal account, an account with a minimum balance
Do this through a new class that inherits from the original. Make sure it does the following:
    1. Provides for an initial deposit, specified minimum balance, name on account creation.
        for now, don't check to see that the initial deposit meets the minimum requirements
    2. Does not permit a withdrawal that takes the balance below the minimum.
        Return zero for valid withdrawals. Otherwise return 4.
    3. When an instance is printed, print the balance and the minimum required for minimum-balance accounts.
Confirm that the original methods work for the new class.
Note – class variables are referenced through the original class
"""


class BankAccount:  # Top tier class (super class) in Python 2 or 3
    acct_cntr = 0  # Class variable

    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable
        BankAccount.acct_cntr += 1  # Updating class variable

    def __str__(self):
        return f"Account: {self.acctname}\tBalance: ${self.balance}"

    def __eq__(self, other):
        return self.balance == other.balance

    def __del__(self):
        BankAccount.acct_cntr -= 1

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
        if (self.balance - amount < 0) or amount < 0:
            return 4

        print(f"Current Balance: ${self.get_balance()}\t Withdrawal Amount: ${amount}")
        self.balance -= amount
        print(f"New Balance for {self.acctname}: ${self.get_balance()}")
        return 0


class MinBalanceAcct(BankAccount):
    def __init__(self, name, minimum, initial):   # This method runs during instantiation
        super().__init__(name)
        self.min_balance = minimum
        self.balance = initial

    def __str__(self):
        return f"Account: {self.acctname}\tMinimum Balance: ${self.min_balance}\tBalance: ${self.balance}"

    def withdrawal(self, amount):
        if (self.balance - amount < self.min_balance) or amount < 0:
            return 4

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

    z = MinBalanceAcct("Larry", 100, 100)
    print(z.acctname)
    z.print_balance()

    ret_code = z.withdrawal(50)
    if ret_code > 0:
        print("Withdrawal failed")
    print(z)


if __name__ == '__main__':
    main()