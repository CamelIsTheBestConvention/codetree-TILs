n = int(input())
bae = 1
cnt = 0

while True:
    print(n*bae, end=' ')
    if n*bae % 5 == 0:
        cnt += 1
    if cnt == 2:
        break
    
    bae += 1