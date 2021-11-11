# https://www.codewars.com/kata/570f6436b29c708a32000826/python


def first_non_repeated(s):
	for c in s:
		if s.count(c) == 1:
			return c

