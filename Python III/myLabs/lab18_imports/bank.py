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
    min_acct_cntr = 0

    def __init__(self, name, minimum, initial):   # This method runs during instantiation
        super().__init__(name)

        if initial < minimum:
            raise ValueError("Insufficient initial deposit")

        self.min_balance = minimum
        self.balance = initial
        MinBalanceAcct.min_acct_cntr += 1

    def __str__(self):
        return f"Account: {self.acctname}\tMinimum Balance: ${self.min_balance}\tBalance: ${self.balance}"

    def __del__(self):
        MinBalanceAcct.min_acct_cntr -= 1

    def withdrawal(self, amount):
        if (self.balance - amount < self.min_balance) or amount < 0:
            return 4

        print(f"Current Balance: ${self.get_balance()}\t Withdrawal Amount: ${amount}")
        self.balance -= amount
        print(f"New Balance for {self.acctname}: ${self.get_balance()}")
        return 0
