numbertests = int(input())
price = []
saved = 0
total = 0

for i in range(0, numbertests):
    price.append(int(input()))

for x in price:
    total += int(x)

price.sort(reverse=True)

for i in range(0, numbertests):
    if (i + 1) % 3 == 0:
        saved += int(price[i])

print(total - saved)
