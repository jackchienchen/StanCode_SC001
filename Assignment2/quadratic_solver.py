"""
File: quadratic_solver.py
Name: Jack Chen
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This function figures out the roots of the input number.
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	if b**2 - 4 * a * c > 0:
		root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (a * 2)
		root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (a * 2)
		print('Two Roots: ' + str(root1) + " , " + str(root2))
	elif b ** 2 - 4 * a * c == 0:
		root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (a * 2)
		print('One Root: ' + str(root1))
	elif b ** 2 - 4 * a * c < 0:
		print('No Root')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
