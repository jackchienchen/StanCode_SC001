"""
File: prime_checker.py
Name: Jack Chen
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	This function figures out if the input number is a prime number.
	"""
	print('Welcome to prime checker!')
	while True:
		x = int(input('n: '))
		if x == EXIT:
			print('Have a good one!')
			break
		if prime_check(x) is True:
			print(str(x) + ' is not a prime number.')
		else:
			print(str(x) + ' is a prime number.')
	print('Have a good one!')


def prime_check(n):
	for i in range(2, n):
		if n % i == 0:
			return True
	return False


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
