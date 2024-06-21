a, b = map(int, input().split())

for i in range(a, b+1):
    if a > b:
        break

    if a % 2 == 1:
        print(a, end=' ')
        a *= 2
    else:
        print(a, end=' ')
        a += 3