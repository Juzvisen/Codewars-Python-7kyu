# https://www.codewars.com/kata/578de3801499359921000130/python


def two_by_two(animals):
	return {x:2 for x in animals if animals.count(x) > 1} if animals else False

