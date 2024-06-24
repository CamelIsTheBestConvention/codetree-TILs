a, b, c = map(int, input().split())
cnt = a

for i in range(a, b+1):
    if cnt == b:
        print("NO")
        break

    if c % i == 0:
        print("YES")
        break
    else:
        cnt += 1
        continue