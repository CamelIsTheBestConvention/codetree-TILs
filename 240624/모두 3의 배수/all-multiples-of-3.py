exist = False

for i in range(5):
    a = int(input())

    if a % 3 == 0:
        exist = True
    else:
        break

if exist:
    print(1)
else:
    print(0)