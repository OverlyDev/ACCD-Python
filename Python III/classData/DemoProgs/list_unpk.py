"""Unpack a Collection

This program demonstrates how the ability to unpack a list or string
can be very useful in keeping your code clean and eliminating
the use of some indices.
"""


my_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for a, b, c in my_lst:
    print(a, b, c)

ltrs = 'abcd'
w, x, y, z = ltrs
print(w, x, y, z)

ltrs2 = ['abc', 'def', 'ghi']
for a1, a2, a3 in ltrs2:
    print(a1, a2, a3)
