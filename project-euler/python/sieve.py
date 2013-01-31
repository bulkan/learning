## {{{ http://code.activestate.com/recipes/117119/ (r2)
# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002

from math import sqrt
from itertools import ifilter, permutations

def eratosthenes():
    ''' Yields the sequence of prime numbers via the Sieve of Eratosthenes.
     http://code.activestate.com/recipes/117119/
    '''

    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality

    while True:
        p = D.pop(q, None)
        if p:
            x = p + q
            while x in D: x += p
            D[x] = p
        else:
            D[q*q] = q
            yield q
        q += 1


def primes_up_to(n):
    """Generates all primes less than n."""
    if n <= 2: return
    yield 2
    F = [True] * n
    seq1 = xrange(3, int(sqrt(n)), 2)
    seq2 = xrange(seq1[-1] + 2, n, 2)
    for p in ifilter(F.__getitem__, seq1):
        yield p
        for q in xrange(p * p, n, 2 * p):
            F[q] = False
    for p in ifilter(F.__getitem__, seq2):
        yield p




def get_primes(n):
    for i in eratosthenes():
        if i > n: break
        yield i



if __name__ == '__main__':

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
 
    o = 600851475143
    n = 13195
    primes  = list(primes_up_to(n))
    max = None
    import pdb; pdb.set_trace() 
    for p in permutations(primes, len(primes)):
        print p
        

        #if p > n: break
        #if n%p == 0 and p > max:
        #    max = p

    print max






