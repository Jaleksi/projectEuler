#
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
#


def main():
    total = 0
    with open("digits.txt", "r") as txt:
        for rivi in txt.readlines():
            tmp = ""
            for numero in rivi.replace("\n", ""):
                tmp += numero
            total += int(tmp)
    print(str(total)[0:10])


if(__name__ == "__main__"):
    main()
