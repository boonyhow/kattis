from sys import stdin

numbertest = int(input())

for i in range(0, numbertest):
    blank = input()
    numberofstudent = int(input())
    candies = 0
    for j in range(0, numberofstudent):
        candies += int(input())
    if candies % numberofstudent == 0:
        print("YES")
    else:
        print("NO")