# https://www.codewars.com/kata/56582133c932d8239900002e/python


def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0