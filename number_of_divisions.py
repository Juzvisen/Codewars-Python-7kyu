# https://www.codewars.com/kata/5913152be0b295cf99000001/python

from math import log

def divisions(n,divisor):
	return int(log(n, divisor))


print(divisions(6,2))