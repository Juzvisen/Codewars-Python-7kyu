# https://www.codewars.com/kata/55f9064161541a9e01000001/python


import re

def valid_number(n):
    return bool(re.fullmatch('[+-]?\d*\.\d\d', n)


print(valid_number("10.00"))

