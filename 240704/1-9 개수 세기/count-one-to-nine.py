n = int(input())
arr = list(map(int, input().split()))
arr2 = [0] * 9

for i in range(n):
    arr2[arr[i]-1] += 1

for i in range(len(arr2)):
    print(arr2[i])