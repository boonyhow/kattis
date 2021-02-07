out = []

for i in range(1, 6):
    name = input()
    x = name.find("FBI")
    if x != -1:
        out.append(str(i))

if len(out) == 0:
    print("HE GOT AWAY!")
else:
    print(' '.join(out))