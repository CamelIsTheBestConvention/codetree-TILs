sum = 0
cnt = 0

while True:
    a = int(input())

    if a < 20 or a > 29:
        print("%.2f" % (sum/cnt))
        break
    else:
        sum += a
        cnt += 1