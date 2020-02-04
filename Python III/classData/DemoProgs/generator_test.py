"""Two different ways to use a generator.
         
The first test takes care of the next method and StopIteration for you
by using "for."  It uses the generator as an iterable.  The second
test uses the next function to invoke the __next__ method of the iterable
and has to test for StopIteration to detect when the generator has
finished.  
"""

def yld_tst(cnt_dn):
    i = cnt_dn
    while i >= 0:
        yield i
        i -= 1

for z in yld_tst(10):  # As an iterator
    print(z, end=' ')
print('\nyld_tst finished')
    
nxt_gen = yld_tst(10)
while True:   # By directly accessing each item in order
    try:
        print(next(nxt_gen), end=' ')
    except StopIteration:
        print('\nyld_tst2 finished')
        break


