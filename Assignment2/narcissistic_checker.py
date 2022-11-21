"""
File: narcissistic_checker.py
Name: Jack Chen
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    TODO:
    """
    print('Welcome to the narcissistic number checker!')
    while True:
        x = int(input('n: '))
        if x == EXIT:
            break
        else:
            if nar_checker(x) == x:
                print(str(x) + ' is a narcissistic number')
            else:
                print(str(x) + ' is not a narcissistic number')
    print('Have a good one!')


def nar_checker(num):
    nar_num = 0
    digit = count_digit(num)
    while num > 0:
        last_digit = num - (num // 10) * 10
        nar_num += last_digit**digit
        num = num // 10
    return nar_num


def count_digit(num):
    digit = 0
    while num > 0:
        digit += 1
        num = num // 10
    return digit


if __name__ == '__main__':
    main()
