# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/python


def solve(s):
	return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()
	

