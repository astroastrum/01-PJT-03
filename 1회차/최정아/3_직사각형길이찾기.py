import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 직사각형의 변의 길이 저장
rec_1 = {
    "a": 4, 
    "b": 3, 
    "c": 4
}

# 정사각형 변의 길이 저장
rec_2 = {
    "a": 5, 
    "b": 5, 
    "c": 5
}

# 사각형의 test_case 마다 돌아가면서 길이 b와 a 꺼냄
for test_case in rec_1:
    print("b")
    for test_case in rec_2:
        print("a")
# 변의 길이 출력
print("b", "a")