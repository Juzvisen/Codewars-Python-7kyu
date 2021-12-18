# https://www.codewars.com/kata/563089b9b7be03472d00002b/python


class List(object):
    def remove_(self, integer_list, values_list):
        blacklist = set(values_list)
        return [val for val in integer_list if val not in blacklist]