"""
File: rocket.py
Name: Jack
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# you can control the length of each separate parts of the rocket
SIZE = 3


def main():
	"""
	All the functions together can build up a rocket.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	:param m: the length/size of the rocket
	you can build the rocket's head depending on the param.
	"""
	n = 1
	m = SIZE
	for k in range(m):
		for i in range(m):
			print(' ', end='')
		for j in range(n):
			print('/', end='')
		for o in range(n):
			print('\\', end='')
		print('')
		n += 1
		m -= 1


def belt():
	"""
	:param SIZE: is to decide the length of the belt.
	the belt is the part to connect the rocket's head and body.
	"""
	print('+', end='')
	for i in range(SIZE):
		print('==', end='')
	print('+')


def upper():
	"""
	:param SIZE: is to decide the length of the upper body.
	The upper body of the rocket is compose with (|),(.),(/),(\)
	To withstand the weight of the rocket, (|) will be use once every level
	on the right and left side.
	(.) will be lessen every level, started with n-1 dots.
	the number of (/\) will depend on the constant SIZE, SIZE = number of /\
	"""
	m = SIZE - 1
	n = 1
	for i in range(SIZE):
		print('|', end='')
		for j in range(m):
			print('.', end='')
		for k in range(n):
			print('/\\', end='')
		for j in range(m):
			print('.', end='')
		print('|', end='')
		m -= 1
		print('')
		n += 1


def lower():
	"""
	:param SIZE: is to decide the length of the lower body.

	The lower body of the rocket is compose with (|),(.),(/),(\)
	To withstand the weight of the rocket, (|) will be use once every level
	on the right and left side.
	(.) will be added by one every level, started with 0 dots.
	the number of (\/) will depend on the constant SIZE, SIZE = number of \/
	"""
	m = SIZE
	n = 0
	for i in range(SIZE):
		print('|', end='')
		for j in range(n):
			print('.', end='')
		for k in range(m):
			print('\\/', end='')
		for j in range(n):
			print('.', end='')
		print('|', end='')
		print('')
		m -= 1
		n += 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()