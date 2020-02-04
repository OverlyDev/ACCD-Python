"""
Write a generator that duplicates the range function for positive numbers only
It should be able to accept 1 to 3 arguments which correspond to the same arguments for range()
You should NOT check the validity of the individual arguments
Make sure there are a valid number of arguments
If the number of arguments is incorrect, print an error message, and issue a return to shut down the generator
You can use the starter program generator2.py
Hint: The generator itself is a very small loop. Most of the code goes into setting up the variables
    Make sure you understand the implications of receiving one, two, or three arguments
"""


def main():
    print("0 arguments")
    for i in gen_range():
        print(i, end=" ")

    print("1 argument")
    for i in gen_range(1):
        print(i, end=" ")
    print()

    print("2 arguments")
    for i in gen_range(1, 2):
        print(i, end=" ")
    print()

    print("3 arguments")
    for i in gen_range(69, 75, 1):
        print(i, end=" ")
    print()

    print("4 arguments")
    for i in gen_range(69, 75, 1, 42):
        print(i, end=" ")


def gen_range(*args):
    if len(args) < 1 or len(args) > 3:
        print("Too little or too few arguments")
        return False

    if len(args) == 1:
        start = 0
        stop = args[0]
        while start <= stop:
            yield start
            start += 1

    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        while start < stop:
            yield start
            start += 1

    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        while start < stop:
            yield start
            start += step


if __name__ == '__main__':
    main()
