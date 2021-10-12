# https://www.codewars.com/kata/59ff4709ba2a14501500003a/python


def arrange(arr):
    return sorted(arr, key=lambda k: int(k.replace('T','000000').replace('KG','000').replace('G','')))

