name = input()
list = []
output = []
for i in name:
    list.append(i)
for j in range(0,(len(list) - 1)):
    if list[j] != list[j + 1]:
        output.append(list[j])
output.append(list[-1])
print("".join(output))