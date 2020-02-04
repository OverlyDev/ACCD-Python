"""File opened as w+

When you open a file as w+, the file is treated as new, the same
as opening with the option w.  The difference here is that when you are
finished writing the file, you can set the file to the beginning with
seek(0) and read the records. Again, if you do a write while reading,
the new records go to the end of the file.  Read operations resume
where they left off.
"""

with open('c:/pydata/tmpprecip2012.dat', 'r') as fin,  \
     open('c:/pydata/readwritetest.dat', 'w+') as fout:
    for cnt in range(5):  # Extract 5 records from a text file for testing
        line = fin.readline()
        fout.write(line)
        print('{0!r}'.format(line))
    print()

    fout.seek(0)  # Reset to the beginning of the file
    for line in fout:  # Read the records with a for statement
        print('{0!r}'.format(line))  # Verify what has been read
        fout.write('0000000000.00000\n')  # Add new records with write

    print()
    fout.seek(0)
    for line in fout:  # Print the whole file
        print('{0!r}'.format(line))

