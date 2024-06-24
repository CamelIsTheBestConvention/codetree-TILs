a = int(input())

for i in range(a):
    for j in range(i+1):
        print('*', end='')
    print()
    print()

for i in range(a-1):
    for j in range(a-1,i, -1):
        print('*', end='')
    print()
    print()