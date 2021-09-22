# https://www.codewars.com/kata/609eee71109f860006c377d1/python


def last_survivor(letters, coords):
	l = [ x for x in letters]
	[l.pop(x) for x in coords]
	return l[0]

