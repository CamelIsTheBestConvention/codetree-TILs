a = int(input())

for i in range(1, a+1):
    for j in range(a-i):
        print(' ', end='')
    for k in range(i):
        print('*', end=' ')
    print()

for i in range(1, a):
    for j in range(i):
        print(' ', end='')
    for k in range(a-i, 0, -1):
        print('*', end=' ')
    print()