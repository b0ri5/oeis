from itertools import islice
from sympy import primorial, sieve


def numerator(n):
    return sum((primorial(n) // p for p in islice(sieve, n)))


def sequence(n):
    return numerator(n) - primorial(n)
