# https://www.codewars.com/kata/588e2a1ad1140d31cb00008c/train/python


def generate_pairs(m,n):
	return [(i,j) for i in range(m, n + 1) for j in range(i, n + 1)]


