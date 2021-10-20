# https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6


def sort_by_binary_ones(num_list):
	return sorted(num_list, key = lambda k: (-bin(k).count("1")))

