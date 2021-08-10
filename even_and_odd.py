# https://www.codewars.com/kata/594adadee075005308000122/python


def even_and_odd(n):
	ne = "".join(x for x in str(n) if x in "02468")
	no = "".join(y for y in str(n) if int(y) % 2)
	return tuple(0 if not a else int(a) for a in (ne, no))


