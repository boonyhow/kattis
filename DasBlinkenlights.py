input0 = input()
numbers = input0.split()
number1 = int(numbers[0])
number2 = int(numbers[1])
time = int(numbers[2])
range1 = list(range(1, number1 + 1))
factors1 = list(x for x in range1 if number1 % x == 0)
range2 = list(range(1, number2 + 1))
factors2 = list(x for x in range2 if number2 % x == 0)
common = [x for x in factors1 and factors2 if x in factors1 and factors2]
lcm = int(number1 * number2 / max(common))
if lcm <= time:
    print("yes")
if lcm > time:
    print("no")