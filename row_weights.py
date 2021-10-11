# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9


def row_weights(array):
	team_1 = sum(y[1] for y in enumerate(array,1) if y[0] % 2)
	team_2 = sum(y[1] for y in enumerate(array,1) if y[0] % 2 == 0)
	return team_1, team_2

