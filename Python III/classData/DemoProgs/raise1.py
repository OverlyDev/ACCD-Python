"""Raise Standard Exceptions

Two ways to raise a standard exception and pass information to the
main program. Note the use of the args variable in returning
multiple items.
From Python documentation:
The except clause may specify a variable after the exception name.
The variable is bound to an exception instance with the arguments stored
in instance.args.   For convenience, the exception instance defines
__str__() so the arguments can be printed directly without having to
reference .args.
"""

def deposit1(amt):
    if amt < 1000:
        raise ValueError('Deposit too small' )
    else:
        print('Deposit OK')
    return

def deposit2(amt):
    if amt < 1000:
        raise ValueError('Deposit too small', amt) 
    else:
        print('Deposit OK')
    return

try:
    deposit1(100)
except ValueError as msg:
    print(msg) # Exception has a __str__ method that allows this.
    print(msg.args[0])

try:
    deposit2(100)
except ValueError as msg:
    print(type(msg), type(msg.args), msg)
    print(msg.args[0], '-', msg.args[1])
