# https://www.codewars.com/kata/564d0490e96393fc5c000029/python


def coin_combo(c):
    R = []
    for p in (25, 10, 5, 1):
        R.append(c//p)
        c = c%p
    return R[::-1]



