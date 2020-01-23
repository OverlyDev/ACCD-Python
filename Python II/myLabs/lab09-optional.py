# read tmpprecip.dat and use a dictionary to accumulate the data necessary to report for each year:
#   1. Total rainfall
#   2. Max high temp
#   3. Min high temp
#   4. Avg high temp
#
# use a separate dictionary to report the avg precipitation by month
# create well-formatted reports from each dictionary
# once the program is working, exclude all the data prior to 1970. Then run again exluding all data after 1970
# Note the differences in rainfall totals


def main():
    with open("/home/kek/PycharmProjects/ACCD-Python/Python II/classData/tmpprecip.dat", "r") as f:
        data = f.read().split()

    # per_year(data)

    per_month(data)


def per_year(data):
    years = []
    for i in data:
        if i[4:8] not in years:
            years.append(i[4:8])
    num_years = len(years)

    data_to_report = {}
    for year in years:
        tmp_days, tmp_rain, tmp_max, tmp_min, tmp_avg = 0, 0, 0, 1000, 0

        for line in data:
            if line[4:8] == year:
                tmp_rain += float(line[8:13])
                tmp_avg += int(line[13:16])

                if int(line[13:16]) > tmp_max:
                    tmp_max = int(line[13:16])

                if int(line[13:16]) < tmp_min:
                    tmp_min = int(line[13:16])

                tmp_days += 1

        data_to_report[year] = f"{tmp_rain:.1f} {tmp_max} {tmp_min} {(tmp_avg/tmp_days):.1f}"

    print("Year\t\tRain\t\tMax Hi\tMin Hi\tAvg Hi")
    for k in data_to_report:
        year = k
        rain = data_to_report[k].split()[0]
        max_hi = data_to_report[k].split()[1]
        min_hi = data_to_report[k].split()[2]
        avg_hi = data_to_report[k].split()[3]
        print(year, rain, max_hi, min_hi, avg_hi, sep="\t\t")


def per_month(data):
    months = []
    for i in data:
        if i[0:2] not in months:
            months.append(i[0:2])

    data_to_report = {}
    for month in months:
        tmp_days, tmp_rain = 0, 0

        for line in data:
            if line[0:2] == month:
                tmp_rain += float(line[8:13])
                tmp_days += 1

        data_to_report[month] = f"{(tmp_rain/tmp_days):.2f}"
        print(tmp_days, tmp_rain)


    print(data_to_report)








if __name__ == '__main__':
    main()