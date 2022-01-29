# https://www.codewars.com/kata/563b662a59afc2b5120000c6/python


def nb_year(p0, percent, aug, p):
    t = 0
    while p0 < p:
        p0 = int(p0*(1 + percent/100)) + aug  
        t += 1
    return t