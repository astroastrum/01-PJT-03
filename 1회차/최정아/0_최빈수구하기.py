import sys

sys.stdin = open("_최빈수구하기.txt")

# 케이스의 수 T 주어짐
t = int(input()) 
# 최빈수 초기값
frecuent_n = [0]

for test_case in range(1, t+1):
    test_case = map(int, input().split())
    # 옆에 나열된 숫자와 같다면
    if 1 == (t+1):
        # 최빈수 수에 포함
        frecuent_n += test_case

# T의 숫자를 처음부터 끝까지 돌음
for n in t:
    # idx 1보다 최빈수가 크거나
    if frecuent_n > 1:
        # 최대 점수가 숫자보다 크면
        if max_n < n:
            # 최대 점수를 숫자로 넘김
            max_n = n
        print(max_n)
    
print(t, frecuent_n)