input0 = input()
inputz = input0.split()
numberbox = int(inputz[0])
V = int(inputz[1])
listofvol = []


for i in range(0, numberbox):
    dimensions0 = input()
    dimensions = dimensions0.split()
    volume = int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2])
    listofvol.append(volume)

listofvol.sort()
largest = listofvol[numberbox - 1]
print(largest - V)