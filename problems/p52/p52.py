#
# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.
#


def sameNums(a, b):
    return sorted(str(a)) == sorted(str(b))


def laskuri(n):
    for i in range(2, 7):
        if(sameNums(n, n*i)):
            continue
        else:
            return False
    return True


def main():
    num = 1
    while(not laskuri(num)):
        num += 1
    print(num)


if(__name__ == "__main__"):
    main()
