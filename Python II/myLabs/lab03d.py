# 23 students
# what are the chances two of you have the same birthday
# generate random samples of 1-365 and check for matches
# run this at least 100 times
# at the end, print the number of times duplicate dates were detected
# use the count method to determine whether there are duplicates
# Mathematically, the probability is about 50%
# Your results should be in the area of 40-60%


import random


def main():
    """
    TODO: Actual docstring
    """

    num = 0

    for i in range(100):
        result = birthday()
        if result:
            num += 1

    print(f"Number of duplicates: {(num/100):.0%}")


def birthday():
    """
    TODO: Actual docstring
    """

    listyboi = []

    for i in range(23):
        listyboi.append(random.randrange(1, 365))

    for i in listyboi:
        if listyboi.count(i) > 1:
            return True

    return False


if __name__ == '__main__':
    main()
