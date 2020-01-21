# Using tmpprecip2012.dat
# Accumulate number of days with measurable rainfall
# Get the total rainfall for the year
# Print both of these


def main():
    """
    Reads a file containing a year's rainfall data into memory then:
        1. Counts number of days with measurable rainfall
        2. Calculates total rainfall for the year
    Prints both of these values
    """

    days = 0
    rain = 0

    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/tmpprecip2012.dat", "r") as f:
        data = f.read()
    data = data.split("\n")
    data.pop(len(data) - 1)

    for day in data:
        x = float(day[8:13])
        if x > 0:
            days += 1
            rain += x

    print(f"Rain days = {days}")
    print(f"Rain amount = {rain}")


if __name__ == "__main__":
    main()
