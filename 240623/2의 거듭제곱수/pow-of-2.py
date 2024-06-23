a = int(input())
cnt = 0

while True:
    if a == 1:
        print(cnt)
        break
    else:
        a //= 2
        cnt += 1