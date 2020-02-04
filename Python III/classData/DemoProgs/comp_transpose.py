"""Comprehension Example

This program uses both a comprehension and a loop within a loop
to transpose a two-dimensional list.  From a 4x2 list it creates
a 2x4 list.
"""

matrix = [[1, 2],[3,4],[5,6],[7,8]]

transposed = [[row[i] for row in matrix] for i in range(2)]
print(transposed)

transposed = []
for i in range(2):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


