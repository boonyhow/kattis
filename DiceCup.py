computer0 = input()
compsplit = computer0.split()
N0 = compsplit[0]
M0 = compsplit[1]
N = int(N0)
M = int(M0)
Nlist = []
Mlist = []
sumlist = []
frequency = []
results = []


def func(N, M):
    for x in range(1, N + 1):
        Nlist.append(x)
    for y in range(1, M + 1):
        Mlist.append(y)
    for a in Nlist:
        for b in Mlist:
            sum = a + b
            sumlist.append(sum)
            sumlist.sort()
    for i in range(2, N + M + 1):
        frequency.append(sumlist.count(i))
    highest_freq = max(frequency)
    for j in range(2, N + M + 1):
        if sumlist.count(j) == int(highest_freq):
            results.append(j)


func(N, M)
for x in results:
    print(x)