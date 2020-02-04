"""
Write a program to calculate a factorial recursively
    Reminder: the factorial of a positive integer n is denoted by n!
                it is the product of all positive integers less than or equal to n
                ex: 4! = 4 * 3 * 2 * 1
Your program should receive an integer from the keyboard and use a recursive function to solve it
"""
# TODO: Fix recursive function
import math


def main():
    to_solve = input("Enter a positive integer:\n> ")
    try:
        if to_solve == "q" or to_solve == "Q":
            print("Exiting...")
            quit()

        to_solve = int(to_solve)
        if to_solve > 0:
            print(recursive(to_solve))

    except ValueError:
        print("Invalid input. Try again or press [Q] to quit")
        main()


def recursive(to_solve):

    return to_solve * recursive(to_solve - 1)




if __name__ == '__main__':
    main()
