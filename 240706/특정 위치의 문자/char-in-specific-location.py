arr = ['L', 'E', 'B', 'R', 'O', 'S']
n = input()
notfind = -1

for i in range(len(arr)):
    if n == arr[i]:
        notfind = i
        print(notfind)
    

if notfind == -1:
    print("None")