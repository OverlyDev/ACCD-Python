"""lab_03a_probability_alt.py

This program simulates rolling a pair of dice 100,000 times and
calculates the percentage of the time each possible roll occurs.
The results are produced two different ways as an example.
These results are then compared to the mathematically derived
results.  This program uses only 11 positions in the list.
"""

from random import randrange

roll_lst = 11 * [0]  # positions 0 and 1 will never be used.
rolls = 100000
for i in range(rolls):
    dice_roll = randrange(1, 7) + randrange(1, 7)
    roll_lst[dice_roll - 2] += 1
    
for roll in range(11):
    print('{0:2d} {1:6.2%}'.format(roll + 2, roll_lst[roll] / rolls))
print()

#  OR
roll = 2
for i in roll_lst:
    print('{0:2d} {1:6.2%}'.format(roll, i / rolls))
    roll += 1

    
