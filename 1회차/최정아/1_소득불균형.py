import sys

sys.stdin = open("_소득불균형.txt")

# 테스트 케이스의 수 T 주어짐
T = int(input())
# 테스트 케이스 각각 두 줄로 주어짐
test_case = map(int, input().split())

# 소득 평균
avg = sum(N_income)/len(n)

for test_case in range(1, T+1):
    # 정수의 개수와 소득을 뜻하는 N의 정수가 주어짐
    N = int(input())
    N_income = int(input()) 
    # 평균 이하의 소득을 가진 사람들의 수
    if N_income < avg:
        print('lower_than_average')

print('#x', 'lower_than_average')