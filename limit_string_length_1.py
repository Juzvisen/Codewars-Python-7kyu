# https://www.codewars.com/kata/5208fc3cb613bc725f000142/python


def solution(st, limit):
	if len(st) <= limit:
		return st
	return st[:limit] + "..."

