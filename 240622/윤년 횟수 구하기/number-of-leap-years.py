yun = 0
pung = 0

a = int(input())

for i in range(1, a+1):
    if i % 100 == 0 and i % 400 != 0:
        pung += 1
    elif i % 4 == 0:
        yun += 1
    else:
        pung += 1

print(yun)