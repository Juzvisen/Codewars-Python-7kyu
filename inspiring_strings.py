# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/python


def longest_word(s):
    return sorted(s.split(), key = len)[-1]