#
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832.
#
# Find the thirteen adjacent digits in the 1000-digit number that have
# the greatest product. What is the value of this product?
#


def kertoma(x):
    tulos = 1
    for i in str(x):
        tulos *= int(i)
    return tulos


def main():
    with open("digits.txt", "r") as txt:
        digits = txt.read().replace("\n", "")

    maxValue = 0

    for i in range(len(digits)-13):
        if(kertoma(digits[i:i+13]) > maxValue):
            maxValue = kertoma(digits[i:i+13])
    print(maxValue)


if(__name__ == "__main__"):
    main()
