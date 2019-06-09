#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#


def isPrime(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True


def main():
    pass
    # ??????????????????



if(__name__ == "__main__"):
    main()
