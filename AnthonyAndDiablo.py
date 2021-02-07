from math import pi
from math import sqrt
numbers0 = input()
numbers = numbers0.split()
#A = (pi) ((radius) ** 2)
#((radius) ** 2) = A / pi
radius = sqrt(float(numbers[0]) / pi)
circumference = 2 * pi * radius
if circumference <= float(numbers[1]):
    print("Diablo is happy!")
else:
    print("Need more materials!")