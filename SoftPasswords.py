stored = input()
given = input()

if stored == given:
    print("Yes")
elif given.swapcase() == stored:
    print("Yes")
elif len(given) == (len(stored)-1):
    if given == stored[1:]:
        if stored[0].isdigit():
            print("Yes")
        else:
            print("No")
    if given == stored[0:-1]:
        if stored[-1].isdigit():
            print("Yes")
        else:
            print("No")
else:
    print("No")
