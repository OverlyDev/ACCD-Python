"""lab_06a_count.py

This program counts all of the printable, non-whitespace characters
and prints them out in descending order of occurrence.  The source
data is the book, "Alice in Wonderland."  This version of the program
uses the sorted function directly on the zip results rather than the
sort method which requires a list.
"""

from string import whitespace

char_cnt = {}
#fin = open('/home/student/pydata/alice_in_wonderland.dat', 'r') # Linux
fin = open('c:/pydata/alice_in_wonderland.dat', 'r')  # Windows file
bookin = fin.read()
bookin = bookin.upper()
for char in bookin:
    if char in whitespace:
        continue
    if char in char_cnt:
        char_cnt[char] += 1
    else:
        char_cnt[char] = 1 # Insert char as the key with value 1
fin.close()

unload = sorted(zip(char_cnt.values(), char_cnt.keys()))

iter_count = 0
line_count = 0
for count, character in unload[-1::-1]:
    iter_count += 1
    if iter_count > 30:
        break
    print('{0:s} {1:6,d}   '.format(character, count), end=' ')
#    print(f'{character:s} {count:6,d}   ', end=' ')  # f-string formatting
#    print '%s %6d   ' % (character, count), # Older formatting - Didn't
#           include the thousands separators in this case.
    line_count += 1
    if line_count >= 5:
        line_count = 0
        print()

    
