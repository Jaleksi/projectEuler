#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#

def multisqsum(n): #n = mihin lukuun asti
    yht = 0
    for i in range(1, n+1):
        yht += i**2
    return yht

def multisqsq(n):
    yht = 0
    for i in range(1, n+1):
        yht += i
    return yht**2


def main():
    print(multisqsq(100) - multisqsum(100))


if(__name__ == "__main__"):
    main()
