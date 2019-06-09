#
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25 (numerot X-kuviolla haussa, nurkasta nurkkaan)
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?
#


def laskuri(s): # s = sivun lopullinen mitta
    diagonals = [1]
    luku = 2
    sivu = 3
    while(sivu <= s):
        väli = sivu-2
        for _ in range(4):
            luku += väli
            diagonals.append(luku)
            luku += 1
        sivu += 2
    return sum(diagonals)


def main():
    print(laskuri(1001))


if(__name__ == "__main__"):
    main()
