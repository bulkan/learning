#The nth term of the sequence of triangle numbers is given by, tn = 0.5n(n+1); so the 
#first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical 
#position and adding these values we form a word value. For example, the word value
#for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we
#shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a
# 16K text file containing nearly two-thousand common English words, how many are triangle words?

import math

T = [(0.5*x*(x+1)) for x in xrange(1,200)]

alpha = 'abcdefghijklmnopqrstuvwxyz'


def triangle(n):
    return (n * (n+1) )/ 2


def is_triangle(n):
    return str((math.sqrt(1+8*n)-1) / 2).endswith('.0')


def main():
    f = open('problem42_words.txt')
    words = [w.replace('"','').lower() for w in f.readline()[:-1].split(',')]
    f.close()
    
    triwords = []
    count = 0
    max = 0
    for word in words:
        s = sum([alpha.find(c)+1 for c in word])

        if is_triangle(s):
            count += 1
            print "%s,%d" %(word, s), is_triangle(s)
            triwords.append((word,s))
    print count





if __name__ == '__main__':
    main()
