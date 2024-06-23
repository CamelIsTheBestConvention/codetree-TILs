a = int(input())

for i in range(2, a):
    if a % i == 0:
        print('C')
        break
    if i == (a-1):
        print('N')