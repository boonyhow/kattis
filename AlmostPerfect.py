from sys import stdin
from math import ceil

for line in stdin:
    if line == "" or line == "\n":
        break
    else:
        number = int(line.rstrip())
        factors = 0
        for i in range(2, ceil(number ** 0.5) + 1):
            if number % i == 0:
                factors += i
                factors += (number / i)
                if number - (i ** 2) == 0:
                    factors -= i
                if number % (i-1) == 0 and (i-1) != 1:
                    factors -= i
                    factors -= (number/i)
        factors += 1
        if number == factors:
            print(str(number) + " perfect")
        elif abs(number - factors) <= 2:
            print(str(number) + " almost perfect")
        else:
            print(str(number) + " not perfect")

