"""
File: triangular_checker.py
Name: Jack Chen
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Finds if the input is a triangular number
    """
    print('Welcome to the triangular number checker!')
    x = int(input('n: '))
    while x != EXIT:
        if tri_checker(x) is True:
            print(str(x) + ' is a triangular number')
        else:
            print(str(x) + ' is not a triangular number')
        x = int(input('n: '))
    print('Have a good one!')


def tri_checker(n):
    for i in range(n):
        k = i + 1
        if (k*(k+1))/2 > n:
            return False
        if n == (k * (k + 1))/2:
            return True


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
