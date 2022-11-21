"""
File: weather_master.py
Name: Jack Chen
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

QUIT = -1


def main():
	print("stanCode \"Weather Master 4.0\"!")  # \可以使雙引號中再次出現雙引號
	tem = int(input('Next Temperature: (or -1 to quit)?'))
	if tem == QUIT:
		print('No temperatures were entered.')
	else:
		max_tem = tem
		min_tem = tem
		sum_tem = tem
		count = 1
		cold_day = 0
		if tem < 16:
			cold_day += 1
		while True:
			tem = int(input('Next Temperature: (or -1 to quit)?'))
			if tem == QUIT:
				break
			else:
				if tem > max_tem:
					max_tem = tem
				if tem < min_tem:
					min_tem = tem
				if tem < 16:
					cold_day += 1
				sum_tem += tem
				count += 1
		print('Highest Temperature = ' + str(max_tem))
		print('Lowest Temperature = ' + str(min_tem))
		print('Average = ' + str(sum_tem/count))
		print(str(cold_day) + ' cold day(s)')


if __name__ == "__main__":
	main()
