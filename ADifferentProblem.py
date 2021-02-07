from sys import stdin
for read in stdin:
    x = [read.split()]
    for y in range(0, len(x)):
        number1 = int((x[y])[0])
        number2 = int((x[y])[1])
        diff = abs(number1 - number2)
        print(diff)











#inp = input()
#list = []
#while len(inp) > 0:
#    list.append(inp)
#    inp = input()
#for i in range(0, len(list)):
#    numbers = list[i].split()
#    number1 = int(numbers[0])
#    number2 = int(numbers[1])
#    print(abs(number1 - number2))













#name = input()
#list = []
#for i in name:
#    list.append(i)
#for j in range(1,len(list)):
#    if list[j] == list[j + 1]:
#        list.remove(list[j])
#
#print("".join(list))