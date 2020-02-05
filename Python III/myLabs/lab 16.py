"""
Change the previous program to prevent a minimum balance account from being created without an initial deposit
    that meets the required minimum
Capture the error in the main program and print an appropriate message indicating the problem
The message should contain a description of the problem, the attempted deposit amount, and the minimum requirement
"""

# TODO: FIX EXCEPTIONS. WHAT DO.


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
            raise BankExceptions.min_balance_creation(initial, minimum)

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


class BankExceptions(Exception):
    def __init__(self):
        self.msg = ""

    def min_balance_creation(self, deposit, min_req):
        self.msg = ("Error creating account.",
                    f"Required minimum balance: ${min_req}",
                    f"Deposit amount: ${deposit}"
                    )


def main():
    a = BankAccount('Monty Python')  # Create an instance of Bankaccount
    b = BankAccount('Guido van Rossum')  # Create another instance

    ret_code = a.deposit(500) # Deposit $100 into account a
    if ret_code > 0:
        print('Deposit failed')  # Return > 0

    ret_code = b.deposit(500) # Deposit $500 into account b
    if ret_code > 0:
        print('Deposit failed')  # Return > 0

    z = MinBalanceAcct("Larry", 100, 50)
    print(z.acctname)
    z.print_balance()



if __name__ == '__main__':
    main()
