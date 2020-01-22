# read alice in wonderland into memory
# create a dictionary counting all the printable characters excluding whitespace
# be sure not to count upper and lower case letters separately
# when done, print the top 30 most frequently occurring characters along with the number of occurrences
# if you have time, print five characters/occurrence combinations per line
# make sure all the elements of the printed lines form neat columns

from string import printable, whitespace


def main():
    """
    TODO: Actual Docstring
    """
    occur = {}

    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/alice_in_wonderland.dat", "r") as f:
        data = f.read().upper()

    for c in data:
        if c in printable and c not in whitespace:
            if c in occur:
                occur[c] += 1
            else:
                occur[c] = 1

    x = zip(occur.values(), occur.keys())
    sorted_occur = reversed(sorted(x))

    for cnt, key in sorted_occur:  # TODO: Only print the top 30 results
        print(key, cnt)

    # TODO: Cleanly format the printed output



if __name__ == '__main__':
    main()
