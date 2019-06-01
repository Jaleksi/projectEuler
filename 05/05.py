#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?
#

def divi20(x):
    for i in range(1, 21):
        if(x % i != 0):
            return False
    return True

def main():
    n = 20
    while(True):
        if(divi20(n)):
            break
        else:
            n += 20
    print(n)

if(__name__ == "__main__"):
    main()
