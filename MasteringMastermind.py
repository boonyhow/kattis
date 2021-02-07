input0 = input()
inputs = input0.split()
length = int(inputs[0])
code0 = inputs[1]
code = [x for x in code0]
guess0 = inputs[2]
guess = [x for x in guess0]

#𝑟 = the number of pegs that are identical in both color and position in the code and the guess, and
#𝑠 = the number of remaining pegs that are identical in color but not in the same position.

r = 0
s = 0

compare = list(zip(code, guess))
for (i , j) in compare:
    if i == j:
        r += 1
        code.remove(i)
        guess.remove(j)

code_string = ""
guess_string = ""
code.sort()
guess.sort()
for x in code:
    code_string += x
for y in guess:
    guess_string += y


removal = []
lenofstrings = length - r
for i in range(0, lenofstrings):
    if guess_string.find(code_string[i]) != -1:
        guess_string = guess_string.replace(code_string[i], "0", 1)
        s += 1


print(str(r) + " " + str(s))


