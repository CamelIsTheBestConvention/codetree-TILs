a = int(input())
cnt = 0

while True:
    if a >= 1000:
        print(cnt)
        break

    if a % 2 == 0:
        a = a*3+1
        cnt += 1
    else:
        a = a*2+2
        cnt += 1