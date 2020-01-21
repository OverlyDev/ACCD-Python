# Read Alice in Wonderland into memory
# count all letters regardless of case
# count all cases of letter "e" regardless of case
# print total of all letters, number of e's, and percent of the total that e's comprise
import string


def main():
    """
    Reads an entire file into memory then:
        1. Counts total number of letters, regardless of case
        2. Counts total number of the letter "e", regardless of case
    Prints the total letters, e's, and percentage of e's in the letters
    """

    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/alice_in_wonderland.dat", "r") as f:
        text = f.read()

    # letters, e = count_things(text)
    letters, e = count_no_string(text)
    percent = round((e/letters), 4) * 100

    print(f"Total letters: {letters}")
    print(f"Total e's: {e}")
    print(f"{percent}% of all the letters are e's")


def count_things(text):
    """
    Uses string.ascii_letters because simple
    """

    numLetters = 0
    numE = 0

    for c in text:
        if c in string.ascii_letters:
            numLetters += 1
            if c == "e" or c == "E":
                numE += 1

    return numLetters, numE


def count_no_string(text):
    """
    Uses an actual ASCII comparison to satisfy learning requirement
    """

    numLetters = 0
    numE = 0

    for c in text:
        if ("a" <= c <= "z") or ("A" <= c <= "Z"):
            numLetters += 1
            if c == "e" or c == "E":
                numE += 1

    return numLetters, numE


if __name__ == "__main__":
    main()
