# https://www.codewars.com/kata/57cc79ec484cf991c900018d/solutions


def db_sort(arr): 
    return sorted(arr, key=lambda x: (isinstance(x,str),x))