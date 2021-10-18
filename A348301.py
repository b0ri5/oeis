import sympy

from itertools import islice
from sympy import primorial, sieve


def numerator(n):
    first_n_primes = list(islice(sieve, n))
    return sum((primorial(n) // first_n_primes[i] for i in range(n)))


def sequence(n):
    return numerator(n) - primorial(n)
