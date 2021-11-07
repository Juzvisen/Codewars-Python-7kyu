# https://www.codewars.com/kata/56c2acc8c44a3ad6e400050a/python


def countzero(string):
	return sum(1 if c in "abdegopq069DOPQR" else 2 if c in "%&B8" else 0 for c in string.replace("()","0"))


