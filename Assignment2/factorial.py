"""
File: factorial.py
Name: Jack Chen
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	Input a positive integer, the algorithm will be able to output it's factorial.
	"""
	print('Welcome to stanCode factorial master!')
	while True:
		x = int(input('Give me a number, and I will list the answer of factorial: '))
		if x == EXIT:
			break
		else:
			ans = 1
			for i in range(x):
				ans *= i + 1
			print('Answer: ' + str(ans))
	print('------ See ya! ------')


if __name__ == '__main__':
	main()