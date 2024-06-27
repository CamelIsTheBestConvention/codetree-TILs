def print_stars(n):
    # 첫 번째 줄
    print('* ' * n)
    
    # 중간 부분: 감소 부분
    for i in range(n-1, 0, -1):
        print('* ' * i)
        
    # 중간 부분: 증가 부분
    for i in range(2, n+1):
        print('* ' * i)
        
    # 마지막 줄
    print('* ' * n)

# 사용자로부터 정수 입력 받기
n = int(input("정수 n을 입력하세요: "))

# 별표 출력하기
print_stars(n)