# https://www.codewars.com/kata/5ad29cd95e8240dd85000b54/python


from math import log2

def friends(n):
	return int(log2(max(2,n)-1))


