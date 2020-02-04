"""Raise Unique Exceptions

Create your own exception subclass inheriting from Exception.
You can add data that will be passed to the exception handler.
There are two ways to do this:
1) Actually place varaibles inside the instantiation
2) Return multiple arguments  as a tuple and access them through the class
   with dot notation through the args variable.
From Python documentation:
The except clause may specify a variable after the exception name.
The variable is bound to an exception instance with the arguments stored
in instance.args [which is a tuple].  For convenience, the exception
instance defines __str__() so the arguments can be printed directly
without having to reference .args.
"""

class DepositError(Exception):
    pass   # No code is necessary but at least one statement is required
           # the pass statement satisfies that requirement and does nothing.

def deposit2(amt):    
    if amt < 1000:
        ex = DepositError('Deposit too small', amt, 1000)
        raise ex  # The instance ex is passed to except on a
    else:         # DepositError
        print('Deposit OK')
    return

try:
    deposit2(100)
except DepositError as err1:
    print(type(err1.args), len(err1.args), err1)  # err1 is actually a tuple
    print(err1.args[0], '-', err1.args[1], '  Need at least', err1.args[2])
    print(*err1.args) # Do you remember what the * does in a function call?

