""" lab_03d_dup_dates.py

This program generates 23 random integers in the range 1 to 365
inclusive.  Then it checks to see if any of these numbers, which
represent dates, are duplicates. It does this by sorting the list
and checking all adjacent numbers for duplicates'

See exercise 10-8 on page 118 in **Think Python**
"""

from random import randrange
def has_duplicates(the_list):
    the_list.sort()  # Why is this legal?
    prev = 0
    for day in the_list:
        if day == prev:
            return True
        prev = day
    return False

same_birthday_counter = 0
trials = 100
for trial in range(trials):
    birthdays = []
    for cntr in range(23):
        birthdays.append(randrange(1, 366))
    if has_duplicates(birthdays): # Note: function used as a boolean
        same_birthday_counter += 1
print("{0:d} sets of 23 people had the same birthday in {1:d} trials".format(
    same_birthday_counter, trials))



