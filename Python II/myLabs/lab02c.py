# Use !r to print control characters
# print the character representation of numbers 32 through 126
# iterate through printable variable and print the entry and corresponding ordinal

from string import printable


def main():
    """
    TODO: Actual docstring
    """
    for i in range(32, 127):
        print(f"{chr(i)}", end=' ')

    print()

    for c in printable:
        print(f"{repr(c)}  {ord(c)}")


if __name__ == "__main__":
    main()