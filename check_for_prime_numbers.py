# https://www.codewars.com/kata/53daa9e5af55c184db00025f/python


def is_prime(n):
	return n > 1 and all(n % i for i in range(2, n))


