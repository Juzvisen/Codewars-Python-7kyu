# https://www.codewars.com/kata/541629460b198da04e000bb9/python


def last(*args):
	try:
		return args[-1][-1]
	except:
		return args[-1]
