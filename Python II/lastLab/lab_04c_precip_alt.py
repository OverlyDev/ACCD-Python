"""lab_04c_precip.py

This program reads each record in the tmpprecip.dat file, extracts
the year and the rainfall for each day and accumulates the total
rainfall for each year in a two-dimensional list.  Then it sorts
the data by rainfall amount and prints it.  There is no bad data in
the file. In the real world, clean data is the exception, not the rule.
"""

weather = []
fin = open('c:/pydata/tmpprecip.dat', 'r')
# fin = open('/home/student/pydata/tmpprecip.dat', 'r')
for rec in fin:
    yr = rec[4:8]
    rain = float(rec[8:13])
    for entry in weather:
        if entry[1] == yr:
            entry[0] += rain
            break
    else:
        weather.append([rain, yr])

weather.sort()
for rain, yr in weather:
    print('{0} {1:.2f}'.format(yr, rain))
            
