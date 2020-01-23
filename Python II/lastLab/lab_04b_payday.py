"""lab04b_payday.py

This program processes the two-dimensional list containing the day
of the week and the hours worked for that day.  It recognizes that
Saturday hours are paid at time and a half and Sunday hours are
paid at double time.  It prints the total of the results.

The code is done two ways; first by unpacking each sublist and then
by indexing through each sublist.  In this case the indexing is
unnecessary other than as an exercise to ensure you know how to do it.
"""

pay_rate = 27
week = [['Sunday', 2],
        ['Monday', 8.5],
        ['Tuesday', 6.75],
        ['Wednesday', 9],
        ['Thursday', 9.25],
        ['Friday', 7.75],
        ['Saturday', 7.5]]

total_pay = 0
for day, hours in week: # Unpack the two elements in each sublist
    if day == 'Sunday':  # Double the Sunday hours
        hours = hours * 2
    if day == 'Saturday':
        hours = hours * 1.5  # Saturday hours by half again
    total_pay += hours * pay_rate
print('Pay for the week is ${0:.2f}'.format(total_pay))
            
total_pay = 0
for day_time in week:  # Extract each sublist
    hours = day_time[1]  # Save the hours from the sublist
    if day_time[0] == 'Sunday':
        hours = hours * 2  # Double the Sunday hours
    if day_time[0] == 'Saturday':
        hours = hours * 1.5  # Saturday hours by half again
    total_pay += hours * pay_rate
print('Pay for the week is ${0:.2f}'.format(total_pay))
            
