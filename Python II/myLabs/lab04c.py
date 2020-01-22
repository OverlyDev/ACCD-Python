# use tmpprecip.dat
# accumulate in a two-dimensional list the total precipitation by year


def main():
    """
    TODO: Actual doctstring
    """

    totalRain = []

    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/tmpprecip.dat", "r") as f:
        data = f.readlines()

    for line in data:
        year = line[4:8]
        rain = float(line[8:13])

        for i in totalRain:
            if i[0] == year:
                i[1] += rain
                break
        else:
            totalRain.append([year, rain])

    for i in totalRain:
        print(f"{i[0]} {i[1]:.2f}")


if __name__ == '__main__':
    main()
