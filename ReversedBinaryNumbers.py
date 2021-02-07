binar0 = [x for x in bin(int(input()))]
binar0.remove(binar0[1])
binar0.remove(binar0[0])
binar0.reverse()
binar0.insert(0, "b")
binar0.insert(0, "0")
print(int(("".join(binar0)), 2))
