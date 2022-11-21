"""
File: number_checker.py
Name: Jack Chen
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
    """
    TODO:
    """
    print('Welcome to the number checker!')
    while True:
        x = int(input('n: '))
        if x == EXIT:
            break
        else:
            y = find_root(x)
            if x == y:
                print(str(x) + ' is a perfect number')
            elif x > y:
                print(str(x) + ' is a deficient number')
            elif x < y:
                print(str(x) + ' is a abundant number')
    print('Have a good one!')


def find_root(n):
    ans = 0
    for i in range(1, n):
        if n % i == 0:
            ans += i
    return ans


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
