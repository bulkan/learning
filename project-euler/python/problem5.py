#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

import itertools

def main():
    found = False
    for n in itertools.count(1):
        for i in range(2,20):
            if n % i != 0:
                found = False
                break
            else: found = True
        if found:
            print n
            return


if __name__ == '__main__':
    main()

