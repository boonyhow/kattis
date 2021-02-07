numbertest = int(input())

for i in range(0, numbertest):
    instruction = input().split()
    if len(instruction) > 2:
        if instruction[0] == "simon" and instruction[1] == "says":
            print(" ".join(instruction[2:]))
        else:
            print('\n')
    else:
        print('\n')

