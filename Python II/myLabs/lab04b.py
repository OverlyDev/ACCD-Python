# Use unpack and index index methods
# using payday.py
# process the data in the list and produce a report showing the total pay for the week
# 27$/hr, day of the week, hours worked to the nearest .25 hr
# hours worked M-F = normal pay
# Sat = time and a half
# Sun = double time

from pprint import pprint


def main():
    """
    TODO: Actual docstring
    """

    pay_rate = 27
    week = [['Sunday', 2],
            ['Monday', 8.5],
            ['Tuesday', 6.75],
            ['Wednesday', 9],
            ['Thursday', 9.25],
            ['Friday', 7.75],
            ['Saturday', 7.5]]

    using_unpack(week, pay_rate)
    print()
    using_indexes(week, pay_rate)


def using_unpack(week, pay_rate):
    """
    TODO: Actual docstring
    """

    print("Using unpack")
    paycheck = 0

    for i, j in week:
        if i == "Saturday":
            paycheck += pay_rate * 1.5 * j
        elif i == "Sunday":
            paycheck += pay_rate * 2 * j
        else:
            paycheck += pay_rate * j

    print(f"Pay for the week is ${paycheck:.2f}")


def using_indexes(week, pay_rate):
    """
    TODO: Actual docstring
    """

    print("Using indexes")
    paycheck = 0

    for i in week:
        if i[0] == "Saturday":
            paycheck += pay_rate * 1.5 * i[1]
        elif i[0] == "Sunday":
            paycheck += pay_rate * 2 * i[1]
        else:
            paycheck += pay_rate * i[1]

    print(f"Pay for the week is ${paycheck:.2f}")


if __name__ == '__main__':
    main()