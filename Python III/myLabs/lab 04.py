# modify the results of lab 03 to print just the top 20 words along with their respective use counts
# print them in descending order by use count
# do the sorting in one statement using the capabilities we have just reviewed
# unload the dictionary with the items method and sort those results directly
# some code later int he program needs to be changed; determine what that is

from string import punctuation


def main():
    with open('/home/kek/PycharmProjects/ACCD-Python/Python III/classData/words.txt', 'r') as fin:
        temp = fin.read().splitlines()
        words = {}.fromkeys(temp, 0)  # initialize all dictionary counters to zero
    # print('Words in dictionary - {0:,d}'.format(len(words)))

    unfound_words = []  # List to keep words not located in dictionary.
    with open('/home/kek/PycharmProjects/ACCD-Python/Python III/classData/alice_in_wonderland.dat', 'r') as fin:
        bookin = fin.read().lower()  # read in the entire book and lower the case

    replace_chars = str.maketrans(punctuation, len(punctuation) * ' ', "'")
    bookin = bookin.translate(replace_chars)
    wordlist = bookin.split()
    # print('Words in book - {0:,d}'.format(len(wordlist)))
    for word in wordlist:
        if word in words:
            words[word] += 1  # If found, increment counter, otherwise
        else:
            unfound_words.append(word)  # add to list of unfound words

    top_20 = reversed(sorted(zip(words.values(), words.keys())))

    print('\n', 'TOP 20 WORDS'.center(13), '\n')
    print("Word\t\tCount")
    count = 0
    for i, j in top_20:
        if count < 20:
            print(f"{j:12s}{i:,d}")
            count += 1

    print("\n", "We're done!".center(13))


if __name__ == '__main__':
    main()
