# read in tmpprecip2012.dat
# create a 2d list to allow for by month:
#   1. Avg high temp
#   2. Max high temp
#   3. Min high temp
# once that works, try it with tmprecip.dat. (over 100 years of data)

from pprint import pprint

BIG = 0


def main():
    """
    TODO: Actual docstring
    """

    # Make our initial list of months 1 - 12
    months = []
    for i in range(12):
        months.append([i+1, 0, 0, 1000, 0])  # month, avg, high, min, days

    if BIG:
        print("We're going big!\n")
        with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/tmpprecip.dat", "r") as f:
            data = f.readlines()

    else:
        with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/tmpprecip2012.dat", "r") as f:
            data = f.readlines()

    for line in data:
        month = int(line[0:2])
        temp = int(line[13:16])

        if temp > months[month-1][2]:
            months[month-1][2] = temp

        if temp < months[month-1][3]:
            months[month-1][3] = temp

        months[month-1][1] += temp  # Adding up the temperatures for future averaging

        months[month - 1][4] += 1  # Adding up the number of days for future averaging

    # Calculate the average temp for each month
    for month in months:
        month[1] = month[1]/month[4]

    print("Month\tAverage\t\tHigh\tMin")
    for i in months:
        print(f"{i[0]}\t\t{i[1]:.2f}\t\t{i[2]}\t\t{i[3]}")


if __name__ == '__main__':
    main()
