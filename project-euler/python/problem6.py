#The sum of the squares of the first ten natural numbers is,

#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import itertools
import math

def main():
    sum = 0
    sum_square = 0

    for n in itertools.count(1):

        sum_square += math.pow(n, 2)
        sum += n

        if n == 100: break

    print math.pow(sum, 2) - sum_square 





if __name__ == '__main__':
    main()

