#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
#

def charPoints(name, sijainti):
    points = sum([ord(char.lower())-96 for char in name])
    return points * sijainti


def main():
    with open("names.txt", "r") as txt:
        names = sorted(txt.read().replace('"', '').replace(',', ' ').split())

    print(sum([charPoints(name, names.index(name)+1) for name in names]))


if(__name__ == "__main__"):
    main()
