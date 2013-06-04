def main():
    numbers = open('50_digit_numbers.txt')
    s = sum([int(n) for n in numbers])
    print s
    print str(s)[:10]


if __name__ == '__main__':
    main()
