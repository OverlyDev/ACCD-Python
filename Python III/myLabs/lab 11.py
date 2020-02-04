"""
Using class.py:
Create a new method to provide the balance for any account that's passed
    Test it by retrieving the current balances for both accounts and printing them
    Replace the current code that reaches inside the instance without using a method

Create a method for withdrawals. Subtract the withdrawal amount from the balance.
    This method should not allow a withdrawal that would result in a negative balance
    return a code of 4 for an invalid withdrawal and a zero for valid withdrawal
    test with valid and invalid amounts for one account
    then print the resulting balances for that account
"""


class BankAccount:  # Top tier class (super class) in Python 2 or 3
    def __init__(self, name):   # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable

    def deposit(self, amount):     # another method
        if amount < 0:
            return 4   # Negative deposits are really withdrawals
        self.balance += amount
        return 0        # Deposit successful

    def get_balance(self):
        return self.balance

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
    ret_code = a.deposit(100) # Deposit $100 into account a
    if ret_code > 0:
        print('Deposit failed')  # Return > 0
    ret_code = b.deposit(500) # Deposit $500 into account b
    if ret_code > 0:
        print('Deposit failed')  # Return > 0

    print(f"Balance for {a.acctname}: ${a.get_balance()}")
    print(f"Balance for {b.acctname}: ${b.get_balance()}")

    ret_code = a.withdrawal(100)
    if ret_code > 0:
        print("Withdrawal failed")

    ret_code = a.withdrawal(100)
    if ret_code > 0:
        print("Withdrawal failed")

    print(a)

if __name__ == '__main__':
    main()