"""Comprehension with If/Else

This program demonstrates the way if/else constructs can be
used within a comprehension.  This particular example examines
each entry in a list containing numbers.  For numbers >= 45,
one is added to the new number.  Otherwise, five is added to
the new number.  At some point in time, you have to decide
whether the compact expression of the comprehension introduces
too much difficulty in reading your code.
"""

lst = [22, 13, 45, 50, 98, 69, 43, 44, 1]

# Using a comprehension
newlst = [x+1 if x >= 45 else x+5 for x in lst]

print(lst)
print(newlst)

# Using a loop
newlst = []
for x in lst:
    if x >= 45:
        newlst.append(x + 1)
    else:
        newlst.append(x + 5)

print(newlst)
