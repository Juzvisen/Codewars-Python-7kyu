# https://www.codewars.com/kata/61123a6f2446320021db987d/python


def prev_mullt_of_three(n):
	while n % 3:
		n //= 10
	return n or None

