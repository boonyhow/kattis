input0 = input()
input1 = input()
time0 = input1.split()
time = []
output = []
for x in time0:
    y = int(x)
    time.append(y)
time.sort(reverse=True)
for i in range(len(time)):
    time[i] += i + 1


print(max(time) + 1)


#numbers0 = input()
#numbers = numbers0.split()
#if (float(numbers[0]) * 4) == float(numbers[1]):
#    print("Diablo is happy!")
#else:
#    print("Need more materials!")