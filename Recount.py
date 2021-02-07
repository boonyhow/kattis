from sys import stdin

listvotes = []

votecount = {}
for line in stdin:
    if line == "***\n":
        break
    if (line.rstrip()) not in votecount:
        votecount[(line.rstrip())] = 0
    if (line.rstrip()) in votecount:
        votecount[(line.rstrip())] += 1

j = 0
for i in votecount:
    if votecount[i] > j:
        j = votecount[i]

list = []
for i in votecount:
    if votecount.get(i) == j:
        list.append(i)

if len(list) > 1:
    print("Runoff!")
else:
    print(list[0])