from math import ceil
from math import sqrt

number = int(input())
primesinrange = ceil(sqrt(number))
listprimes0 = [x for x in range(primesinrange + 1)]
#range of numbers from 2 to the number itself
listprimes0 = listprimes0[2:]
listprimes1 = [y for y in range(ceil(sqrt(primesinrange)) + 1)]
listprimes1 = listprimes1[2:]
#finding the primes within the range of numbers
for j in listprimes1:
    for i in listprimes0:
        if i == j:
            continue
        if i % j == 0:
            listprimes0.remove(i)
count = 0
#counting number of divisors
for a in listprimes0:
    while number % a == 0:
        number = number / a
        count += 1

#in case number is a prime number or co primes, or the remainder is a prime thats no longer divisible
if number != 1:
    count += 1


print(count)