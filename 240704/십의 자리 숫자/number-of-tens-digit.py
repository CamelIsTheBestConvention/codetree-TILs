arr = list(map(int, input().split()))
arr2 = [0] * 9

for i in range(len(arr)):
    if arr[i] == 0:
        break
    
    cnt = arr[i] // 10

    if cnt == 0:
        continue
    else:
        arr2[cnt-1] += 1

for i in range(len(arr2)):
    print("%d - %d" % (i+1, arr2[i]))