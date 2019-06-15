#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
#
# Find the sum of the digits in the number 100!
#


def fact(n):
    factorial = n
    for i in range(n-1, 0, -1):
        factorial *= i

    return factorial


def sumOfDigits(n):
    return sum(int(i) for i in str(n))


def main():
    print(sumOfDigits(fact(100)))


if(__name__ == "__main__"):
    main()
