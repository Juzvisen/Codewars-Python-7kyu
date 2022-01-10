# https://www.codewars.com/kata/619f200fd0ff91000eaf4a08/python


def odd_or_even(n):
    if (n%2 != 0):
        return "Either"
    elif ((n/2)%2) == 0:
        return "Even"
    return "Odd"