#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
#


def isPal(x):
    return str(x) == str(x)[::-1]


def binary(n):
    return str(bin(n))[2::]


def main():
    dp = [i for i in range(1, 1000_000) if(isPal(i) and isPal(binary(i)))]
    print(sum(dp))


if(__name__ == "__main__"):
    main()
