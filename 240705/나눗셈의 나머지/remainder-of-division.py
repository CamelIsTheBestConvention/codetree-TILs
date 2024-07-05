def calculate_remainder_square_sum(a, b):
    remainder_counts = [0] * b
    
    while a > 1:
        remainder = a % b
        remainder_counts[remainder] += 1
        a //= b
    
    square_sum = sum(count ** 2 for count in remainder_counts)
    return square_sum

# 입력 받기
a, b = map(int, input().split())

# 결과 계산 및 출력
result = calculate_remainder_square_sum(a, b)
print(result)