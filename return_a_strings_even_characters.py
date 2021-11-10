# https://www.codewars.com/kata/566044325f8fddc1c000002c/train/python


def even_chars(st):
	if len(st) > 100 or len(st) < 2:
		return "invalid string"
	else:
	 	return [x for x in st[1::2]]

