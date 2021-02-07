computer0 = input()
compsplit = computer0.split()
x = int(compsplit[0])
y = int(compsplit[1])
n = int(compsplit[2])
a = [int(b) for b in range(1, n + 1)]

for i in a:
    if i % y == 0:
        a[i - 1] = "Buzz"
    if i % x == 0:
        if i % y == 0:
            a[i - 1] = "FizzBuzz"
        else:
            a[i - 1] = "Fizz"

for i in a:
    print(i)
