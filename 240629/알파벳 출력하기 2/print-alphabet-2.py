n = int(input())
cc = 65

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n, i, -1):
        if cc > 90:
            cc = 65
        print(chr(cc), end=' ')
        cc += 1
    print()