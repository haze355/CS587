import random
import sys

# convert to candidate key according to wisconsin benchmark paper
def convert(uni):
    result = list('A'*7)
    i = 6
    while uni > 0:
        rem = uni % 26
        result[i] = chr(ord('A')+rem)
        uni = uni // 26
        i -= 1
    result.reverse()
    return "".join(result) + "x" * 45

# generate string4
def stringFour(tupCount):
    i = tupCount
    if i % 4 == 0:
        return "A" * 4 + "x" * 48
    elif i % 4 == 1:
        return "H" * 4 + "x" * 48
    elif i % 4 == 2:
        return "O" * 4 + "x" * 48
    else:
        return "V" * 4 + "x" * 48


def generate_relation(tupCount, fileName):
    f = open(fileName, 'w')
    uni = random.sample(range(tupCount), tupCount)
    for i in range(tupCount):
        unique1 = uni[i]
        unique2 = i
        two = unique1 % 2
        four = unique1 % 4
        ten = unique1 % 10
        twenty = unique1 % 20
        onePercent = unique1 % 100
        tenPercent = unique1 % 10
        twentyPercent = unique1 % 5
        fiftyPercent = unique1 % 2
        unique3 = unique1
        evenOnePercent = onePercent * 2
        oddOnePercent = onePercent * 2 + 1
        stringu1 = convert(unique1)
        stringu2 = convert(unique2)
        string4 = stringFour(i)
        print(unique1, unique2, two, four, ten, twenty, onePercent, tenPercent,
              twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent,
              stringu1, stringu2, string4, sep=",", file=f)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python wb.py 1000 onektup.csv")
    tupCount = int(sys.argv[1])
    fileName = sys.argv[2]
    generate_relation(tupCount, fileName)






