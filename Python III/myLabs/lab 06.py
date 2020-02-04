"""
Use range(-40, 120, 10) as input. Assume the values in the range represent Fahrenheit temperatures
The comprehensions should calculate the corresponding Centigrade temperature ( C = 5.0/9.0 *(F - 32))
Create three comprehensions:
    1. a list of tuples containing each C/F pair. Exclude the entries for F temps 0 and 50
    2. a set of tuples containing each C/F pair. Exclude the entries for F temps 0 and 50
    3. dictionary with F temps as keys and C temps as values. Exclude the entries for F temps 0 and 50
"""


def main():
    list_temps = [(to_c(x), f"{x}F") for x in range(-40, 120, 10) if x != 0 and x != 50]
    set_temps = {(to_c(x), f"{x}F") for x in range(-40, 120, 10) if x != 0 and x != 50}
    dict_temps = {f"{x}F": to_c(x) for x in range(-40, 120, 10) if x != 0 and x != 50}

    print("List:\n", list_temps)
    print("Set:\n", set_temps)
    print("Dict:\n", dict_temps)


def to_c(temperature):
    return f"{round((temperature - 32) * 5.0/9.0, 2)}C"


if __name__ == '__main__':
    main()
