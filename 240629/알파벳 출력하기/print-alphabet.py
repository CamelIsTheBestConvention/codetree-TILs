n = int(input())
cc = 65

for i in range(n):
    for j in range(i+1):
        if cc > 91:
            cc = 65
        print(chr(cc), end='')
        cc += 1
    print()