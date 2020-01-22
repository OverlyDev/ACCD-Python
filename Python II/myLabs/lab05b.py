from sys import argv


def main():
    print(f"Collecter argument: {argv}\t type: {type(argv)}")
    for i in range(1, len(argv)):
        try:
            input_temp = float(argv[i])
            nutmp = 5.0 / 9.0 * (input_temp - 32)
            print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
                input_temp, nutmp))

        except Exception as e:
            print(f"Invalid data: {argv[i]}")


if __name__ == '__main__':
    main()
