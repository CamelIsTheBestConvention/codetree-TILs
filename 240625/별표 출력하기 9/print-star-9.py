a = int(input())

for i in range(1, a+1):
    for front in range(a-i, 0, -1):
        print(' ', end=' ')

    for j in range(i*2-1):
        print('*', end=' ')

    for back in range(a-i, 0, -1):
        print(' ', end=' ')

    print()