#
# In the 20×20 grid below, four numbers along a diagonal line have been 
# marked in red.
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?
#


def rivitarkistus(r):  # r = tarkistettavat rivit
    maxProd = 0

    for rivi in r:
        for nro in range(len(rivi)):
            numerot = rivi[nro:nro+4]
            tmp = 1
            for i in numerot:  # Vaakatason tarkistus
                tmp *= int(i)
            if(tmp > maxProd):
                maxProd = tmp

            try:
                tmp = 1
                for i in range(4):  # Pystytasossa tarkistus
                    tmp *= int(r[r.index(rivi)+i][nro])
                if(tmp > maxProd):
                    maxProd = tmp

                tmp = 1
                for i in range(4):  # Vinotarksistus \-suunnassa
                    tmp *= int(r[r.index(rivi)+i][nro+i])
                if(tmp > maxProd):
                    maxProd = tmp

                tmp = 1
                for i in range(4):  # Vinotarkistus /-suunnassa
                    tmp *= int(r[r.index(rivi)+i][nro-i])
                if(tmp > maxProd):
                    maxProd = tmp

            except IndexError:
                pass


    return maxProd


def main():
    rivit = []
    with open("grid.txt", "r") as txt:
        for rivi in txt.readlines():
            rivit.append(rivi.replace("\n", "").split())

    print(rivitarkistus(rivit))


if(__name__ == "__main__"):
    main()
