def is_palindrome(s):
    if len(s) % 2 == 0:
        m = len(s) / 2
        return s[:m] == ''.join(reversed(s[m:]))
    else:
        m = len(s) / 2 + 1
        return s[:m] == ''.join(reversed(s[m-1:]))



def product_palindrome():
    max = 0
    seen = set()
    for a in xrange(999,100, -1):
        seen.add(a)
        for b in xrange(999, 100, -1):
            if b in seen: continue
            p = a*b
            s = str(p)
            if is_palindrome(s) and p > max:
                max = p
                print a,"*",b, s
    print max



if __name__ == '__main__':
    product_palindrome()
