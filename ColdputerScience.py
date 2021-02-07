input0 = input()
temp0 = input()
temp1 = temp0.split()
temp = []
for x in temp1:
    y = int(x)
    temp.append(y)

i = 0
for a in temp:
    if a < 0:
        i += 1

print(i)