"""lab_04c_precip.py

This program reads each record in the tmpprecip.dat file, extracts
the year and the rainfall for each day and accumulates the total
rainfall for each year in a two-dimensional list.  Then it sorts
the data by year and prints it.  There is no bad data in the file.
In the real world, clean data is the exception, not the rule.
"""

weather = []
fin = open('c:/pydata/tmpprecip.dat', 'r')
# fin = open('/home/student/pydata/tmpprecip.dat', 'r')
for rec in fin:
    yr = rec[4:8]
    rain = float(rec[8:13])
    for entry in weather:
        if entry[0] == yr:
            entry[1] += rain
            break
    else:
        weather.append([yr, rain])

weather.sort()
for yr, rain in weather:
    print('{0} {1:.2f}'.format(yr, rain))
            
