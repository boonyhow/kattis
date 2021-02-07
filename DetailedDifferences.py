numbertest = int(input())

for a in range(0, numbertest):
    output = []
    line1 = input()
    line2 = input()
    compare = list(zip(line1, line2))
    for (i , j) in compare:
        if i == j:
            output.append(".")
        if i != j:
            output.append("*")
    print(line1)
    print(line2)
    print("".join(output))
    print("\n")
