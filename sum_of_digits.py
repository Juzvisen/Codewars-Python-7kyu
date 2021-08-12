# https://www.codewars.com/kata/59cf805aaeb28438fe00001c


def sum_of_digits(digits):
	d = str(digits)
	return "" if digits is None else f'{" + ".join(x for x in d)} = {sum(map(int, d))}'
	

)