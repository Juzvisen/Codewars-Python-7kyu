# https://www.codewars.com/kata/582cb3a637c5583f2200005d/python


def get_weight(name):
	return sum(ord(a) for a in name.swapcase() if a.isalpha())


