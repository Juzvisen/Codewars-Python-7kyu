# https://www.codewars.com/kata/604517d65b464d000d51381f/python


def strange_math(n, k):
    return sorted(range(n+1), key=str).index(k)