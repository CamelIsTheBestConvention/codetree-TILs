n = int(input())

for i in range(n):
    a = int(input())
    cnt = 0

    while True:

        if a == 1:
            print(cnt)
            break

        if a % 2 == 0:
            a //= 2
            cnt += 1
        else:
            a = a*3+1
            cnt += 1