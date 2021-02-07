input0 = input()
numbers = input0.split()
number1 = int("".join(list(reversed([x for x in numbers[0]]))))
number2 = int("".join(list(reversed([y for y in numbers[1]]))))
if number1 > number2:
    print(number1)
if number2 > number1:
    print(number2)
