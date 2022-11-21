"""
File: hailstone.py
Name: Jack Chen
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program is able to process the Hailstone sequence.
    You will insert a random number and the program
    will be able to decompose the process and find out how many steps it took.
    """

    print('This program computes Hailstone sequence.')

    x = int(input('Enter a number: '))
    steps = 0

    if x == 1:
        """
        The exceptional circumstance that the first number is 1.
        """
        print('It took 0 steps to reach to 1.')
    else:
        while x != 1:
            if x % 2 == 1:
                """
                When the inserted number is odd: the number *3+1.
                This counted as one step.
                """
                x = int(3*x+1)
                steps = steps + 1
                print(str(int((x-1)/3)) + ' is odd, so I make 3x+1: ' + str(x))
            elif x % 2 == 0:
                """
                When the inserted number is even: the number doubles.
                This counted as one step.
                """
                x = int(x/2)
                steps = steps + 1
                print(str(int(2*x)) + ' is even, so I take half: ' + str(x))
        print(' ')
        print('It took ' + str(steps) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
