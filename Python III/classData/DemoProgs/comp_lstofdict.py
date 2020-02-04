"""Comprehension for list of dicts

This sample is from the Stack Overflow site.  It is intended to process
a list of dictionaries.  It uses a comprehension to extract all of the keys
from the dictionaries into a list.  It then uses a set to extract counts
of all the unique keys.  The original code in Stack Overflow was
unnecessarily complicated.  I have simplified it here
"""

# input dictionaries

d = [{"abc":"movies", "xyz": "sports"}, {"abc": "music", "xyz": "music",
   "pqr":"music"}, {"pqr":"movies"},{"pqr":"sports"}, {"pqr":"news"},
   {"pqr":"sports", "abc": "sports"}]

# fetch keys
b = [j for i in d for j in i.keys()]
print(b)

# print output
for k in set(b):
    print("{0}: {1}".format(k, b.count(k)))
