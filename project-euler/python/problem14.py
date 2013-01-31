"""The following iterative sequence is defined for the set of positive integers:

n => n/2 (n is even)
n => 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

#from multiprocessing import Process
from multiprocessing import Pool

def collatz(n):
    n_orig = n
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = ((3 * n) + 1)
        count += 1
    return (n_orig,count)


if __name__ == '__main__':
    p = Pool(2)
    max = None
    max_n = None
    for n, count in p.map(collatz, range(1000000)):
        if count > max:
            max = count
            max_n = n

    print max_n, max





