numbertest = int(input())
output = []
for a in range(0, numbertest):
    numbers = [int(x) for x in input().split()]
    numlen = numbers[0]
    listofdifference = []
    for i in range(1, numlen):
        diff = abs(numbers[i] - numbers[i + 1])
        listofdifference.append(diff)
    if all(x == listofdifference[0] for x in listofdifference):
        output.append("arithmetic")
    elif not all(x == listofdifference[0] for x in listofdifference):
        numbers = sorted(numbers[1:])
        numbers.insert(0, numlen)
        listofdifference = []
        for i in range(1, numlen):
            diff = abs(numbers[i] - numbers[i + 1])
            listofdifference.append(diff)
        if all(x == listofdifference[0] for x in listofdifference):
            output.append("permuted arithmetic")
        elif not all(x == listofdifference[0] for x in listofdifference):
            output.append("non-arithmetic")

print("\n".join(output))