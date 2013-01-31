#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

def sqr(n):
    return n*n
    #return math.pow(n, 2)


def triplets():
    for a in xrange(1, 1000):
        #if a % 3 != 0 or a % 4 != 0: continue
        for b in xrange(1, 1000):
            #if b % 3 != 0 or b % 4 != 0: continue
            for c in xrange(1, 1000, 2):
                if b % 3 != 0: continue
                if (sqr(a) + sqr(b)) == sqr(c): # and a + b + c == 1000:
                    s = a + b + c
                    print a,b,c,'\t', s

                    if s == 1000:
                        print 'FOUND'
                        return

if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()
    triplets()
    elapsed = datetime.now() - start
    print elapsed

