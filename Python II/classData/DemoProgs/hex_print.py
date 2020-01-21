"""Print Data in Hex

Only binary numbers can be printed using the hex (x) format.
So, convert each character to a binary number using the ord
function.  Then use 02x to format each character taking two
positions and zero padding any character that only produces
one hex digit (such as \n).  This is just one way to produce
a hex printout of your data.
"""


x = 'text;123\t\n'
for y in x:
    print(f'{ord(y):02x}', end = ' ')
