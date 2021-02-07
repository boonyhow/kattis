from sys import stdin


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


for line in stdin:
    if line == "" or line == "\n":
        break
    alphabets = [x for x in line.rstrip()]
    alphabets.sort()
    alphabets = ''.join(alphabets)
    list = []
    repeaters = 1
    list.append(alphabets[0])
    for a in range(1, len(alphabets)):
        if alphabets[a] != alphabets[a - 1]:
            repeaters = repeaters * (factorial(alphabets.count(alphabets[a - 1])))
        newstring = "".join(list)
        if newstring.find(alphabets[a]) == -1:
            list.append(alphabets[a])
    repeaters = repeaters * (factorial(alphabets.count(alphabets[-1])))
    newstring = "".join(list)
    total = factorial(len(alphabets))
    print(total//repeaters)

