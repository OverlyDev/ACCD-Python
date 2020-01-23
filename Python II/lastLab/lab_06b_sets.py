""" lab_03d_dup_dates.py

This program generates 23 random integers in the range 1 to 365
inclusive.  Then it checks to see if any of these numbers, which
represent dates, are duplicates. It does this by adding the dates
to a set which automatically removes duplicates. If the length of the
resulting set is less than the number of people/birthdays being
tested, there were duplicate dates generated.
Also, this version of the program is more general in that you can
easily change the number of people/birthdays being tested.  Note that
there are several ways to get a well-formated line printed.
See exercise 10-8 on page 118 in **Think Python**
"""

from random import randrange

same_birthday_counter = 0
trials = 100
people = 23
for trial in range(trials):
    bday_set = set()  # initialize an empty set
    for b in range(people):
        birthday = randrange(1, 366)
        bday_set.add(birthday)
    if len(bday_set) < people: 
        same_birthday_counter += 1

print(same_birthday_counter, 'sets of', people,
      'people had the same birthday in', trials, 'trials')


