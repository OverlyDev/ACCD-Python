""" Initial class exercise

This is the intial program using classes.  The class (BankAccount)
allows opening an account.  When the instance is created, the name must
be supplied.  Deposits are handled through the method of that name and
must be positive amounts.
"""

class BankAccount:  # Top tier class (super class) in Python 2 or 3
# class BankAccount:  # works fine in Python 3.  Parens not required

    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable
    def deposit(self, amount):     # another method
        if amount < 0:
            return 4   # Negative deposits are really withdrawals
        self.balance += amount
        return 0        # Depost successful

a = BankAccount('Monty Python')  # Create an instance of Bankaccount
b = BankAccount('Guido van Rossum')  # Create another instance
ret_code = a.deposit(100) # Deposit $100 into account a
if ret_code > 0:   
    print('Deposit failed')  # Return > 0
ret_code = b.deposit(500) # Deposit $500 into account b
if ret_code > 0:   
    print('Deposit failed')  # Return > 0
print(a.balance, b.balance) # This is not good code. We will replace it.





