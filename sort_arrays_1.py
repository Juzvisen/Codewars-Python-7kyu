# https://www.codewars.com/kata/594093784aafb857f0000122/train/python


def diff(a, b):
	return sorted(set(a).symmetric_difference(b))

