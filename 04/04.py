#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 
# 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#


def isPal(n):
    return str(n) == str(n)[::-1]



def main():
    maxPal = 0
    for i in range(999):
        for j in range(999):
            x = i * j
            if(isPal(x) and (x) > maxPal):
                maxPal = x

    print(maxPal)



if(__name__ == "__main__"):
    main()
