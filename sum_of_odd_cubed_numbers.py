# https://www.codewars.com/kata/580dda86c40fa6c45f00028a/python


def cube_odd(arr):
    return sum( n**3 for n in arr if n % 2 ) if all(type(n) == int for n in arr) else None