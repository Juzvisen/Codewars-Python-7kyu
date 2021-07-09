# https://www.codewars.com/kata/581214d54624a8232100005f


def matrix(array):
	s = array.copy()
	for i in range(len(s)):
		if s[i][i] >= 0:
			s[i][i] = 1
		else:
			s[i][i] = 0
	return s