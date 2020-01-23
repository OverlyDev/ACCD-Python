"""lab_03a_probability.py

This program simulates rolling a pair of dice 100,000 times and
calculates the percentage of the time each possible roll occurs.
The results are produced two different ways as an example.
These results are then compared to the mathematically derived
results.  This program can be run under Python version 2.  You
should know why the results are so different.
"""

from random import randrange

roll_lst = 13 * [0]  # positions 0 and 1 will never be used.
rolls = 100000
for i in range(rolls):
    dice_roll = randrange(1, 7) + randrange(1, 7)
    roll_lst[dice_roll] += 1
    
for roll in range(2, 13):
    print('{0:2d} {1:6.2%}'.format(roll, roll_lst[roll] / rolls))
print()

#  OR
roll = 2
for i in roll_lst[2:]:
    print('{0:2d} {1:6.2%}'.format(roll, i / rolls))
    roll += 1

    
