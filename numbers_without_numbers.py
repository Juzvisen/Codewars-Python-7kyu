# https://www.codewars.com/kata/6098205ca76224000d62a2d0


one = len("a")
two = len("aa")
three = len("aaa")
four = len("aaaa")
five = len("aaaaa")

def numbers_without_numbers():
	return int(f"{three}{two}{one}{five}{one}{four}{three}{two}{five}")


