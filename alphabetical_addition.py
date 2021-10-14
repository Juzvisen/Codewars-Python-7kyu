# https://www.codewars.com/kata/5d50e3914861a500121e1958/python


def add_letters(*letters):
    return chr((sum(ord(c)-96 for c in letters)-1)%26 + 97)

