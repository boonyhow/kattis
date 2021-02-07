computer0 = input()
compsplit = computer0.split()
counter = []
while computer0.isupper() == False:
    computer0 = input()
while len(compsplit) > 80:
    computer0 = input()

for i in compsplit:
    counter.append(compsplit.count(i))
if max(counter) == 1:
    print("yes")
else:
    print("no")
