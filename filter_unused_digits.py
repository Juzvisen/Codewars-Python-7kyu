# https://www.codewars.com/kata/55de6173a8fbe814ee000061


def unused_digits(*numbers):
	s = "".join(str(x) for x in numbers)
	return "".join(x for x in "0123456789" if x not in s)





