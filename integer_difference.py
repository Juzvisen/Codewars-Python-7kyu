# https://www.codewars.com/kata/57741d8f10a0a66915000001/python


def int_diff(arr, n):
	num = 0
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if abs (arr[i] - arr[j]) == n:
				num += 1

	return num

