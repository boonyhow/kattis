input_1 = input()
input_2 = input()

intro = input_1.split()
num_items = intro[0]
min_price = int(intro[1])
price0 = input_2.split()
price = []
for x in price0:
    y = int(x)
    price.append(y)
length = len(price)
price.sort()


i = 1
output = 1


if length == 1:
    output = 1
if length > 1:
    while price[i] + price[i - 1] <= min_price:
        i += 1
        output += 1
        if i == length:
            break


print(output)