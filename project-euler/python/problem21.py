from collections import defaultdict
from operator import mul


def d(n):
    ''' my initial naive approach '''
    return sum([i for i in range(1, n) if n % i == 0])


def factorization(n):
    """
    Generate the prime factorization of n in the form of pairs (p, k)
    where the prime p appears k times in the factorization.

    >>> list(factorization(1))
    []
    >>> list(factorization(24))
    [(2, 3), (3, 1)]
    >>> list(factorization(1001))
    [(7, 1), (11, 1), (13, 1)]
    """
    p = 1
    while p * p < n:
        p += 1
        k = 0
        while n % p == 0:
            k += 1
            n /= p
        if k:
            yield p, k
    if n != 1:
        yield n, 1


def sum_of_divisors(n):
    """
    Return the sum of divisors of n.

    >>> sum_of_divisors(1)
    1
    >>> sum_of_divisors(33550336) // 2
    33550336
    """
    return reduce(mul, ((p ** (k + 1) - 1) / (p - 1)  for p, k in factorization(n) ), 1) - n

d = sum_of_divisors


def main():
    amicable = defaultdict()

    #n = 220
    #print list(factorization(n))
    #print sum_of_divisors(n)
    #print d(n)

    for n in range(2, 10001):
        a = d(n)
        b = d(a)

        if b == n and a != b:
            amicable[n] = a

    print sum(amicable.values())

if __name__ == '__main__':
    main()
