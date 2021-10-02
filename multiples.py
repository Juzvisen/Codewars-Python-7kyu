# https://www.codewars.com/kata/55a8a36703fe4c45ed00005b/train/python


def multiple(x):
	return "Bang" * (x % 3 == 0) + "Boom" * (x % 5 == 0) or "Miss"

