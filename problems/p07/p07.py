#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?
#

# SUPERHIDAS/-HUONO 

def isPrime(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True


def main():
    primeCount = 0
    n = 1
    while(primeCount < 10001):
        if(isPrime(n)):
           primeCount += 1
        n += 1

    print(primeCount, n)
if(__name__ == "__main__"):
    main()
