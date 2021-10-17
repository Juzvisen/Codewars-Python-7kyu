# https://www.codewars.com/kata/596b8a3fc4cb1de46b000001/python


def center(string, width, fill=' '):
    d = max(width - len(string), 0)
    return fill * ((d + 1) // 2) + string + fill * (d // 2)


