# https://www.codewars.com/kata/595519279be6c575b5000016/python


def battle(x, y):

    # Compute x score using Unicode
    x_value = sum(ord(char) - 64 for char in x)

    # Compute y score using Unicode
    y_value = sum(ord(char) - 64 for char in y)

    if x_value < y_value:
        return y

    if x_value > y_value:
        return x

    return "Tie!"