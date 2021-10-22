from math import gcd
from sympy import primorial


def brute_force(n):
    return sum(
        gcd(r, primorial(n)) == 1 and gcd(r + 2, primorial(n)) == 1
        for r in range(0, primorial(n)))
