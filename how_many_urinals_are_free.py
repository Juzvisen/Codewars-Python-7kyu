# https://www.codewars.com/kata/5e2733f0e7432a000fb5ecc4/python


def get_free_urinals(urinals):
	if urinals.count("11"): return -1
	return urinals.replace("10", "1").replace("01","1").replace("00","0").count("0")
