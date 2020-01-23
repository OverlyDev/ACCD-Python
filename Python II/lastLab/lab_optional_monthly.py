"""lab_optional.py

This program reads the temperature/precipitation data for San Antonio
for the period 1/1/1900 to 12/31/2016.  The monthly dictionary is used
to accumulate, by month, the
aggregate precipitation.  The average precipitation for each month is
calculated by dividing the aggregate precipitation by the number of
years in the sample.  Note how a set is used to determine the number
of unique years.  Then, one at a time, uncomment the test to exclude
data either before or after 1970.  Note the differences in results.
"""

#fin = open('/home/student/pydata/tmpprecip.dat')
fin = open('c:/pydata/tmpprecip.dat')
mondic = {}

# mondic format: key: month(2 digit); total precip

yr_set = set()
for linein in fin:
    tyr = linein[4:8]
    tmon = linein[0:2]
    if not (tyr.isdigit()and tmon.isdigit()):
        print('Bad Data - {0!r}'.format(linein))
#        print 'Bad Data - %r' % (linein)  # Older formatting
        continue
#    if tyr < '1970':
#        continue
#    if tyr >= '1970':
#        continue
    try:
        precip = float(linein[8:13])
        temp = int(linein[13:16])
        
    except ValueError:
        print('Bad Data - {0!r}'.format(linein))
#        print 'Bad Data - %r' % (linein)  # Older formatting
        continue
    yr_set.add(tyr)
    if tmon in mondic:
        mondic[tmon] += precip
    else:
        mondic[tmon] = precip

years = len(yr_set)
monlst = sorted(mondic.items())
print('\n\n')
tot_precip = 0.0
for mon, precip in monlst:
    tot_precip += precip/years
    print('{0} {1:5.2f}'.format(mon, precip/years))
#    print '%s %5.2f' % (mon, precip/years)  # Older formatting
print('Average Annual Rainfall - {0:.1f}'.format(tot_precip))               
fin.close()
        
