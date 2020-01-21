"""List Change Timer

This program measures the difference between append and
concatenate in lists when dealing with relatively large additions
to a list.  The times increase exponentially for concatenation as the
number of operations increases due to the entire list being moved to
a new location each time.  This program also demonstrates the difference
between elapsed time and CPU time using two different functions from
the time module.
"""

import time
lst = []
start1 = time.perf_counter() # Take initial times
start2 = time.process_time()
for num in range(100000):
    lst.append(num)
print('{0:.3f} CPU seconds this way'.format(
    time.process_time() - start2)) # Subtract intial time from current time.

print('{0:.3f} Total seconds this way'.format(
    time.perf_counter() - start1))

lst = []
start1 = time.perf_counter()
start2 = time.process_time()
for num in range(100000):
    lst= lst + [num]
print('{0:.3f} CPU seconds the other way'.format(
    time.process_time() - start2))
print('{0:.3f} Total seconds the other way'.format(
    time.perf_counter() - start1))



