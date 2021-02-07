numbertest = int(input())

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x -1)


for i in range(numbertest):
    a = factorial(int(input()))
    print(str(a)[-1])