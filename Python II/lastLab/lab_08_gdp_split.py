"""lab_08_gdp_split.py

This program reads the file gdp.txt, separates each item delimited by a
comma, calcualtes the gdp generated per person in each country, sorts them
from largest to smallest and prints the results formatted appropriately.
All the data in this exercise comes from the web and you should not
assume it is accurate.

It also reads the file split.txt, changes all text to lower case, replaces
all punctuation with spaces, splits based on whitespace, prints the length
of the list, eliminates duplicates with a set, prints the length of the set,
creates a list of the set, sorts the list and prints it.  Remember, a
set cannot be sorted in place.
"""

fin = open('c:/pydata/gdp.txt', 'r')
#fin = open('/home/student/pydata/gdp.txt')
gdp_list = []
for x in fin:
    country, tpopulation, tgdp = x.split(',') # unpack the list created by split()
    gdp = float(tgdp)*1000000 # original data is in millions
    gdp_list.append([gdp/int(tpopulation), country])

gdp_list.sort()
for gdp_capita, country in gdp_list[-1::-1]:
    print('{0:20s} {1:,.0f}'.format(country, gdp_capita))
#    print '%-20s %s' % (country, format(gdp_capita, ',.0f')) # Older formats
fin.close()

input('\n\nPress enter to continue:')

from string import punctuation
fin = open('c:/pydata/split.txt', 'r')
#fin = open('/home/student/pydata/split.txt')
txt_in = fin.read().lower()
for x in punctuation:
    txt_in = txt_in.replace(x, ' ')
word_lst = txt_in.split()
word_set = set(word_lst)
print('Words in text:', len(word_lst))
print('Unique words in text:', len(word_set))
word_sort = sorted(word_set)
for entry in word_sort:
    print(entry)

fin.close()


