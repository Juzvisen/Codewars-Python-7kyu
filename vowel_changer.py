# https://www.codewars.com/kata/597754ba62f8a19c98000030/python


def vowel_change(t, v):
    for c in 'aeiou': 
    	t = t.replace(c, v)
    return t