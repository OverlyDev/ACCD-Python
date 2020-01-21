"""lab_01_dice.py

This program simulates a street craps game.  It is designed to demonstrate
the use of loops and decision making structures.  Note the use of the
randrange function instead of the less-Pythonic randint.  It is
important to know the difference between the two.
"""

from random import randrange 
def dice_rolls():
    return randrange(1,7) + randrange(1,7) 

money = 100
plays = 0
contin = 'y'
print('Beginning Balance = ${0:,d}'.format(money))
# print 'Beginning Balance = $%d' % money  # Older formatting
while contin == 'y' or contin == 'Y': # Loop that controls the game
    plays = plays + 1
    win_lose = ''  # This is an empty string until there is a win or loss
    myroll = dice_rolls()
    print(myroll, end=' ')
    if myroll == 7 or myroll == 11:
        win_lose = 'W'
    elif myroll < 4 or myroll == 12:
        win_lose = 'L'
    else:
        point = myroll
        while win_lose == '':
            myroll = dice_rolls()
            print(myroll, end=' ')
            if myroll == 7:
                win_lose = 'L'
                continue
            if myroll == point:
                win_lose = 'W'
                continue
    if win_lose == 'L':
        money = money - 10  # or money -= 10
        print('You lose!')
        if money <= 0:
            break
    if win_lose == 'W':
        money = money + 10
        print('You win!')
    print('Balance = ${0:,d}'.format(money), end=' ')
    contin = input('Play again? y/n: ') # Any entry other than y or Y ends play

print('\nNumber of plays -', plays)
print(f'Ending Balance = ${money:,d}')  # Newest (requires Python 3.6)
print('Ending Balance = ${0:,d}'.format(money))  # Newer formatting
print('Ending Balance = $%d' % money)  # Older formatting
        
    
        
            
