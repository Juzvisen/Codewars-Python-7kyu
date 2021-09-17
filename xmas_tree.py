# https://www.codewars.com/kata/577c349edf78c178a1000108/python


def x_mas_tree(n):
	return [("#"*(x*2-1)).center(n*2-1,"_") for x in list(range(n))+[0]*2]




