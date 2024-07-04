arr = list(map(int, input().split()))
arr2 = [0] * 6

for i in range(len(arr)):
    arr2[arr[i]-1] += 1

for i in range(len(arr2)):
    print("%d - %d" % (i+1, arr2[i]))