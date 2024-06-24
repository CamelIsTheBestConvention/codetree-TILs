a = int(input())

for i in range(a):
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(a-1):
    for j in range(a-1-i, 0, -1):
        print('*', end=' ')
    print()