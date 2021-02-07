input0 = input()
output0 = []

for x in input0:
    if x.isupper():
        output0.append(x)

print("".join(output0[::1]))


