"""Sorting by Count

This program creates a dictionary containing counters.  Then it
unloads the values and keys separately and zips the two together
with the count preceding the key.  Then the sorted function is used
to sort each tuple in ascending order by count.  Finally, the list
created by sorted is parsed in a for loop unpacking each tuple and
printing the key and associated value.
"""


d1 = dict(a=123, b=12, c=32, d=7, e=223)
print(d1)
unld = zip(d1.values(), d1.keys())
print(type(unld), list(unld))  # See what zip creates
unld = zip(d1.values(), d1.keys()) # why is this done again?  Comment
                                   # it out and see what happens.
sort_by_count = sorted(unld)
print(sort_by_count)
for cnt, key in sort_by_count:  # Unpack each tuple into two variables.
    print(key, cnt)
