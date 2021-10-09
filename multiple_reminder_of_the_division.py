# https://www.codewars.com/kata/5a2f83daee1aae4f1c00007e/train/python


def is_multiple(a,b):
	remainder = int(a/b * 10 + .5) % 10
	return remainder > 0 and remainder == 0



