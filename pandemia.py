# https://www.codewars.com/kata/5e2596a9ad937f002e510435/python


def infected(s):
	continents = s.split("X")
	total = sum(map(len, continents))
	infected = sum(len(x) for x in continents if "1" in x)
	return infected * 100 / (total or 1)



