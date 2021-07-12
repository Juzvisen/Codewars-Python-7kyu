# https://www.codewars.com/kata/59cd155d1a68b70f8e000117


def middle_me(N, X, Y):
	if N % 2 == 1:
		return X
	else:
		return Y * (N//2) + X + Y * (N/2)



