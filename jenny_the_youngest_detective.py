# https://www.codewars.com/kata/58b972cae826b960a300003e/python



def missing(nums, str):
	str = str.replace (" ", "").lower()
	try:
		return "".join(str[i] for i in sorted(nums))
	except:
		return "No mission today"

