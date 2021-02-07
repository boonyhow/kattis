input0 = [int(x) for x in input().split()]
walks = [int(x) for x in input().split()]
bus = [int(x) for x in input().split()]
busintervals = [int(x) for x in input().split()]

time = 0
timeneeded = input0[1]
walkfromhome = walks[0]
firstbus = busintervals[0]

if walkfromhome <= firstbus:
    time += firstbus
else:
    time += firstbus * 2


walkbtwstops = walks[1:-1]
walkbtwstops.append(0)

for i in range(input0[2]):
    time += bus[i]
    time += walkbtwstops[i]

time += walks[-1]

if time <= input0[1]:
    print("yes")
else:
    print("no")