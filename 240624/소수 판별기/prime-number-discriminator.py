a = int(input())
exist = False

for i in range(2, a):
    if a % i == 0:
        exist = True

if exist:
    print('C')
else:
    print('P')