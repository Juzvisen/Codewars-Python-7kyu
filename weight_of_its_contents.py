#https://www.codewars.com/kata/53921994d8f00b93df000bea/python


def content_weight(bottle_weight, scale): 
    a, _, c = scale.split(" ")
    return bottle_weight * int(a) / (int(a) + 1) if c == "larger" else bottle_weight / (int(a) + 1)