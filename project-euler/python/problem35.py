# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import itertools
from sieve import eratosthenes, get_primes, primes_up_to


n = 10004

primes = list(get_primes(n))


import pdb; pdb.set_trace() 




def main():
    count = 0
    for i in primes:
        found = True
        si = str(i)
        found = True
        n = si
        for p in xrange(len(si)):
            n = (n[1:] + n[0])
            if n == si: break
            if int(n) not in primes:
                found = False
                break
            
        if found:
            print i
            count += 1

    print "count: %d" %count



if __name__ == '__main__':
    main()


