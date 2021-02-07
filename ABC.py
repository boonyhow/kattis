numbers0 = input()
order0 = input()
numbers1 = numbers0.split()
numbers = []
for i in numbers1:
    j = int(i)
    numbers.append(j)
numbers.sort()
order = []
for x in order0:
    order.append(x)
A = str(numbers[0])
B = str(numbers[1])
C = str(numbers[2])
for y in range(0, 3):
    if order[y] == "A":
        order[y] = A
    if order[y] == "B":
        order[y] = B
    if order[y] == "C":
        order[y] = C

print((" ".join(order)))
