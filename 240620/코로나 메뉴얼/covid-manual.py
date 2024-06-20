a1, b1 = map(str, input().split())
a2, b2 = map(str, input().split())
a3, b3 = map(str, input().split())

result = 0

if a1 == 'Y' and int(b1) >= 37:
    result += 1
if a2 == 'Y' and int(b2) >= 37:
    result += 1
if a3 == 'Y' and int(b3) >= 37:
    result += 1

if result >= 2:
    print('E')
else:
    print('N')