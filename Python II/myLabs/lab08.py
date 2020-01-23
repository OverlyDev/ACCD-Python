# use the split() method to process the following files: gdp.txt, split.txt
# examine each file and determine how best to separate the various elements to accomplish the assigned task
#
# in the first file, each record has three elements: country name, total pop, and GDP
#   1. Calculate the GDP per person for each country
#   2. Print country and GDP/person in descending order of per-capita GDP. Format professionally.
#
# in the second file:
#   1. determine how many words there are in the file
#   2. how many unique words
#   3. print out each unique word in ascending order
#   be sure to change every alphabet character to one case and remove/replace all punctuation using the replace method

from string import punctuation


def main():
    """
    TODO: 1. FIX do_gdp()  2. Actual docstring
    """
    #do_gdp()
    do_split()


def do_gdp():
    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/gdp.txt", "r") as f:
        countries = f.readlines()
        # gdp = f.read().split("\n")


    # gdp = {}
    # for i in countries:  # index, item
    #     temp = i.strip('\n').split(",")
    #     x = (int(temp[2]) * 1000000) / int(temp[1])
    #     gdp[temp[0]] = int(x)
    #
    # ytho = []
    # for k in gdp:
    #     ytho.append(f"{k}  {gdp[k]}")
    # ytho.sort()
    # print(ytho)

    for x in fin:
        country, tpop, tgdp = x.split('.')
        gdp = float(tgdp) * 1000000
        gdp_list.append(gdp/int(tpop), country)

    gdp_list.sort()
    for gdp_capita, country in gdp_list[-1::-1]:
        print()



def do_split():
    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/split.txt", "r") as f:
        data = f.read().lower()

    for i in punctuation:
        data = data.replace(i, " ")  # for some reason, " " adds a few words compared to ""

    wordsList = data.split()
    wordsSet = set(wordsList)

    print(f"Words in text: {len(wordsList)}")
    print(f"Unique words in text: {len(wordsSet)}")

    # for i in sorted(wordsSet):
    #     print(i)

    print(wordsList)


if __name__ == '__main__':
    main()
