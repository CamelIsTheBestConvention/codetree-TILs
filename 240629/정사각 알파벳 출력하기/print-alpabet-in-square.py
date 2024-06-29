n = int(input())
cc = 65

for i in range(n):
    for j in range(n):
        print(chr(cc), end='')
        cc += 1
    print()