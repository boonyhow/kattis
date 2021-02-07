input0 = input()
input = input0.split()
e = int(input[0])
f = int(input[1])
c = int(input[2])
sum = e + f

output= 0

empty = (sum // c) + (sum % c)
output += sum // c

while empty//c != 0:
    output += empty // c
    empty = (empty // c) + (empty % c)

print(output)