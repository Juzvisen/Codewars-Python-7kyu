# https://www.codewars.com/kata/53e30ec0116393fe1a00060b/python


def distinct(integers):
    return sorted(set(integers), key = integers.index)