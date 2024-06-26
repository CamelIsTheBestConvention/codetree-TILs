a = int(input())

print('* ' * a)

for i in range(1, a):
    print('* ' * i)

for i in range(a-1, 0, -1):
    print('* ' * i)

print('* ' * a)