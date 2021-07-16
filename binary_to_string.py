# https://www.codewars.com/kata/5ab3495595df9ec78f0000b4


def binary_to_string(binary):
	return "".join( chr(int(b, 2)) for b in binary[2:].split("0b"))




