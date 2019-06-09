#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def isCurious(n):
    return sum([factorial(int(i)) for i in str(n)]) == n


def main():
    print(sum([i for i in range(3, 1000_000) if(isCurious(i))]))


if(__name__ == "__main__"):
    main()
