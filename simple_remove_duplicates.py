# https://www.codewars.com/kata/5ba38ba180824a86850000f7/python


def solve(arr):
	return [a for i,a in enumerate(arr) if a not in arr[i+1:]]

