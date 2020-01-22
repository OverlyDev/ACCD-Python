# change this program to accept a variable number of temperatures per function call and process all of them
# print the collector argument and its type
# use isinstance to verify the type of each parameter as you iterate through
# each parameter should be either int or float. reject all others. test with invalid data


def fahrenheit_to_centigrade(*args):
    print(f"Collecter argument: {args}\t type: {type(args)}")
    for xtmp in args:
        if isinstance(xtmp, (int, float)):
            nutmp = 5.0 / 9.0 * (xtmp - 32)
            print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
                xtmp, nutmp))

        else:
            print(f"{xtmp} is not valid data")


temp = 72
fahrenheit_to_centigrade(temp)
fahrenheit_to_centigrade(72, -10.5, 'a', 111, 55, True, False, None)
