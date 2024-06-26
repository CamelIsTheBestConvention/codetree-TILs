a = int(input())

for i in range(1, a+1):
    for j in range(i):
        if i % 2 == 1:
            print('*', end=' ')
            break
        else:
            print('*', end=' ')

    print()