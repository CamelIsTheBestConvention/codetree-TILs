n = int(input())

for i in range(n*2+1):
    if i % 2 == 0:
        for i in range(n*2+1):
            print('*', end=' ')
    else:
        for i in range(n+1):
            print('*', end=' ')
            print(' ', end=' ')
    
    print()