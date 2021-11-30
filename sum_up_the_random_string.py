# https://www.codewars.com/kata/55da6c52a94744b379000036/python

import re
def sum_from_string(string):
	d = re.findall("\d+", string)
	return sum(int(i) for i in d)




