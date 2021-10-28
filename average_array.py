# https://www.codewars.com/kata/596f6385e7cd727fff0000d6/python


def avg_arrays(arrs):
	return [sum(a)/len(a) for a in zip(*arrs)]