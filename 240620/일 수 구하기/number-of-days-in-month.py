a = int(input())

if a == 2:
    print(28)
elif (a >= 1 and a <= 7):
    if a % 2 == 1:
        print(31)
    else:
        print(30)
else:
    if a % 2 == 1:
        print(30)
    else:
        print(31)