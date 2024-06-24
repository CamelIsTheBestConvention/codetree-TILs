a = int(input())

for i in range(0, a*2, 2):
    if i > 0:
        for start in range(i//2):
            print(' ', end=' ')

    for j in range(a*2-1, i, -1):
        print('*', end=' ')

    if i > 0:
        for start in range(i//2):
            print(' ', end=' ')
    
    print()