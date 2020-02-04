"""
Use alice_in_wonderland.dat to create a Counter
    1. Read entire file into memory
    2. remove all whitespace using translate/maketrans
    3. use Counter to determine the 20 most used characters in this document
    4. print out each character and its number of occurrences in descending order by use count
    5. be sure to make all cases the same

Alternatively:
    1. use translate and split to isolate each word in the book
    2. use Counter and other tools such as sets to count:
        a. total words in book
        b. unique words
        c. number of words from book not in words.txt
        d. top 20 words in the book by use counts
"""

# TODO: Remove punctuation from number_b. Ensure calculations are actually correct

from collections import Counter
from pprint import pprint
from string import whitespace


def main():
    with open("/home/kek/PycharmProjects/ACCD-Python/Python III/classData/alice_in_wonderland.dat", "r") as f:
        data = f.read().lower()

    # number_a(data)
    number_b(data)


def number_a(input_data: str):
    trans_table = str.maketrans("", "", whitespace)
    data = input_data.translate(trans_table)

    x = Counter(data)

    print("\tTOP 20")
    for i in x.most_common(20):
        print(f"{i[0]}: {i[1]}")

    print("\n\tALL COUNTS")
    for i in x.most_common():
        print(f"{i[0]}: {i[1]}")


def number_b(input_data: str):
    with open("/home/kek/PycharmProjects/ACCD-Python/Python III/classData/words.txt", "r") as f:
        words_all = f.read().lower().split()

    data = input_data.split()
    the_counting = Counter(data)

    total_words = sum(the_counting.values())
    print(f"Total Words: {total_words}")

    unique_words = len(the_counting)
    print(f"Unique Words: {unique_words}")

    print("TOP 20")
    for i in the_counting.most_common(20):
        print(f"{i[0]}:  \t{i[1]}")

    book_words = Counter(list(the_counting))
    dict_words = Counter(words_all)
    book_words = book_words - dict_words
    print(len(book_words))







if __name__ == '__main__':
    main()
