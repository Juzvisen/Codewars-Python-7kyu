# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python


def get_count(input_str):
	return sum(1 for i in input_str if i in "aeiou")


