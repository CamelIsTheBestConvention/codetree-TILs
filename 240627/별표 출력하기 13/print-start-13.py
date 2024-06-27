def print_stars(n):
    # 첫 번째 줄
    print('* ' * n)
    
    # 중간 부분
    for i in range(1, n):
        print('* ' * i)
        print('* ' * (n - i))
    
    # 마지막 줄
    print('* ' * n)

# 사용자로부터 정수 입력 받기
n = int(input())

# 별표 출력하기
print_stars(n)