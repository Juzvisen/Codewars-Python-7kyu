# https://www.codewars.com/kata/5a4138acf28b82aa43000117/python


def adjecent_element_product(array):
	return max (a*b for a, b in zip(array, array[1:]))


print(adjecent_element_product([5, 1, 2, 3, 1, 4]))