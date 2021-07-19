# https://www.codewars.com/kata/5ab3495595df9ec78f0000b4


def binary_to_string(binary):
	return "".join( chr(int(b)) for b in binary[:].split())


print(binary_to_string('01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))




