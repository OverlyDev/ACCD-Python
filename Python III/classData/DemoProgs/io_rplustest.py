"""File opened as r+

When you open a file as r+ you can write to the file as well.  Any
record you write is appended to the end of the file while the read
operations are done sequentially.  When you do a write, the read
operations resume where they left off.
"""

with open('c:/pydata/tmpprecip2012.dat', 'r') as fin,  \
     open('c:/pydata/readwritetest.dat', 'w') as fout:
    for cnt in range(5):  # Extract 5 records from a text file for testing
        line = fin.readline()
        fout.write(line)
        print('{!r}'.format(line))
print()

with open('c:/pydata/readwritetest.dat', 'r+') as finout:
    for line in finout:  # Read one record
        print('{!r}'.format(line)) # Verify all records are read
        finout.write('0000000000.00000\n')  # Write a new record

# Note the order of the records in the modified file
print()
with open('c:/pydata/readwritetest.dat', 'r') as fin:
    for line in fin:
        print('{!r}'.format(line))
