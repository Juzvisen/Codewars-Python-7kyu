# https://www.codewars.com/kata/593406b8f3d071d83c00005d


def count_animals(sentence):
	return sum(int(x) for x in sentence.split() if x.isdigit())

