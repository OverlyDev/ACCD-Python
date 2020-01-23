# Redo lab 03d using an empty set
# place each random number in the set using the add method
# What happens to the duplicates?
# How does this help you determine if there were duplicates?

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

    x = set()

    for i in range(23):
        x.add(random.randrange(1, 365))

    if len(x) < 23:
        return True


if __name__ == '__main__':
    main()
