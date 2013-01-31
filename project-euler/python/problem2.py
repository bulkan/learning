def fib(end):
    p = n = 1
    s = 0
    print n, p ,
    for i in xrange(end):
        c = p + n
        #print c,
        p = n
        n = c

        if c >= 4000000: break

        if c % 2 == 0: s += c
    print s


if __name__ == '__main__':
    fib(4000000)
