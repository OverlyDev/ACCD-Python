"""Simple Recursion

This program uses recursion to sum the numbers in a simple list.  It
also demonstrates how a slice that exceeds the range of the collection
does not result in an index error.  This program is for demonstration
purposes only. We would normally just use the sum function to do this
operation as shown in the last statement.
"""

def sum_it(n):
    print(n)
    if not n:  # An empty variable/collection is false in Python
        return 0
    else:
        return n[0] + sum_it(n[1:])

x = [25, 10, 62, 18]
print(sum_it(x))
print(sum(x))

"""
[25, 10, 62, 18] n[0] = 25, n[1:] = [10, 62, 18]
[10, 62, 18]     n[0] = 10, n[1:] = [62, 18]
[62, 18]         n[0] = 62, n[1:] = [18]
[18]             n[0] = 18, n[1:] = []  Note: no error
115              Sum of all above n[0]'s
"""

