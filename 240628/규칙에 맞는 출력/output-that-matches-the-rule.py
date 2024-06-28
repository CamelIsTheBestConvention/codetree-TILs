n = int(input())
cnt = 0

for i in range(n, 0, -1):
    for j in range(i, n+1):
        print(j, end=' ')
        cnt += 1
    print()