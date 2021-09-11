# https://www.codewars.com/kata/590ac6b9be4dff49b0000042/python


def convert(degrees):
	degree, minutes = divmod(degrees, 1)
	minute, seconds = divmod(minutes * 60, 1)
	second = round(seconds * 60)
	degree = round(degree)
	minute = round(minute)

	if second:
		return [degree, minute, second]
	elif minute:
		return [degree, minute]
	else:
		retrun [degree]

print(convert(80.5))