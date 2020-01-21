# read Alice in Wonderland into memory
# print location of the first occurrence of each word
# print the number of times each word occurs in the book
# determine location of the last occurrence of each word


def main():
    """
    TODO: Actual docstring
    """

    toFind = ["caterpillar", "gryphon", "banana", "spaghetti", "mushroom"]

    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/alice_in_wonderland.dat", "r") as f:
        data = f.read().lower()

    for i in toFind:
        find_word(i, data)


def find_word(word, text):
    """
    TODO: Actual docstring
    """

    # first occurrence
    first = text.find(word)

    # last occurrence
    last = text.rfind(word)

    # number of times
    count = text.count(word)

    # Prints
    if first > 0:
        print(
            f"Word is {word}\n"
            f"The location of the first occurrence is {first}\n"
            f"The location of the last occurrence is: {last}\n"
            f"The number of occurrences is: {count}\n"
        )
    else:
        print(f"{word} was not found.\n")


if __name__ == "__main__":
    main()


