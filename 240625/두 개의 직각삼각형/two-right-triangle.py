a = int(input())

for i in range(a):
    for j in range(a, i, -1):
        print('*', end='')
    if i > 0:
        for k in range(i):
            print(' ', end='')

    if i > 0:
        for k in range(i):
            print(' ', end='')
    for j in range(a, i, -1):
        print('*', end='')

    print()