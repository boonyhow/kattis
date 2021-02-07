numbers = input().split()
numberobstacles = int(numbers[0])
numberfound = int(numbers[1])
listmissed = [x for x in range(numberobstacles)]
for i in range(0, numberfound):
    y = int(input())
    if y in listmissed:
        listmissed.remove(y)

out = numberobstacles - len(listmissed)
listmissed.append("Mario got " + str(out) + " of the dangerous obstacles.")
for i in listmissed:
    print(i)