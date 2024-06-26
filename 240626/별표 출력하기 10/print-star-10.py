a = int(input())

for i in range(a*2):
    if i % 2 == 1:
        for j in range(a-(i-1)//2):
            print('*', end=' ')
    else:
        for j in range(1+(i//2)):
            print('*', end=' ')
    
    print()