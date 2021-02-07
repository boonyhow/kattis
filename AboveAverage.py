numbertest = int(input())



def func():
    scores = []
    input1 = input()
    data = input1.split()
    students = int(data[0])
    for i in range(1, (int(students) + 1)):
        j = int(data[i])
        scores.append(j)
    total = sum(scores)
    average = total / students
    output0 = 0
    for x in scores:
        if x > average:
            output0 += 1
    percent = float(output0 / students)
    return percent


for i in range(1, numbertest + 1):
    output = func() * 100
    print(("{:.3f}".format(output)) + "%")


