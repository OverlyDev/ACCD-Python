# simulate rolling a pair of dice 100,000 times
# accumulate the result of each roll in a  list
# print percentage of times each possible roll occurred

import random as r

ROLLS = 100000


def main():
    """
    TODO: Actual docstring
    """
    rolls = [0] * 11

    for i in range(1, ROLLS + 1):
        d = r.randint(1, 6) + r.randint(1, 6)
        rolls[d-2] += 1

    for x, y in enumerate(rolls):  # x = index, y = value
        # print(f"{x+2}     {y/ROLLS:.2%}")
        length = 10
        p1 = str(x+2)
        p2 = f"{y/ROLLS:.2%}"
        print(f"{p1}{' ' * (length - (len(p1) + len(p2)))}{p2}")


if __name__ == "__main__":
    main()
