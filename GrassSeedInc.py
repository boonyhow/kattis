cost = float(input())
numbertest = int(input())
area = 0

for i in range(0, numbertest):
    sizes = [float(x) for x in input().split()]
    area += (sizes[0] * sizes[1])

print("{0:.7f}".format(area * cost))
