"""
Using the program you created for lab 16, separate the code for the classes from the main program
place the code for the classes in a new directory
give this code module a short name as directed in PEP8
import the code for the classes from that directory
keep in mind whether you want to access the classes through dot notation or not. This governs the import method

use the code on the previous slide to add the new directory to your path temporarily
add a statement to your main program to import your class code
get your program working and pay special attention to the naming requirements
also, examine the code in your new directory
    note the module ending in .pyc. Discussed later hopefully if someone reminds him
"""
import sys


def main():
    # Add local import folder containing bank classes
    sys.path.append('/home/kek/PycharmProjects/ACCD-Python/Python III/myLabs/lab18_imports')
    import bank

    a = bank.BankAccount('Monty Python')  # Create an instance of Bankaccount
    b = bank.BankAccount('Guido van Rossum')  # Create another instance

    ret_code = a.deposit(500) # Deposit $100 into account a
    if ret_code > 0:
        print('Deposit failed')  # Return > 0

    ret_code = b.deposit(500) # Deposit $500 into account b
    if ret_code > 0:
        print('Deposit failed')  # Return > 0

    a.print_balance()

    z = bank.MinBalanceAcct("Larry", 100, 100)
    print(z.acctname)
    z.print_balance()


if __name__ == '__main__':
    main()
