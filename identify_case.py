# https://www.codewars.com/kata/5819a6fdc929bae4f5000a33/python


import re

def case_id(c_str):
    if re.match(r'^([a-z]+\-)+[a-z]+$', c_str):
        return 'kebab'
    if re.match(r'^([a-z]+\_)+[a-z]+$', c_str):
        return 'snake'
    if re.match(r'^([a-z]+[A-Z])+[a-z]+$', c_str):
        return 'camel'
    return 'none'