"""
Using tempconversion.py, replace the function that does the conversion with a lambda
This does require assigning the lambda function to a variable
"""


def main():
    while True:
        temp = input('Enter a temperature: ')
        if temp == 'q' or temp == 'Q':
            break
        try:
            ftemp = float(temp)
        except ValueError:
            print('Input contains non-numeric data - try again')
            continue
        lll = lambda x: 5.0 / 9.0 * (x - 32)
        print('{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
            ftemp, lll(ftemp)))


if __name__ == '__main__':
    main()
