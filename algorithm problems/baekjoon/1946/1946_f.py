import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    result = 0
    
    for i in range(len(arr)):
        count = 0
        person = arr.pop(i)
        for p in arr:
            if person[0] > p[0] and person[1] > p[1]:
                count += 1
        if count == 0:
            result += 1
        arr.insert(i, person)

    print(result)

# 얘는 위에 input 바꿔도 시간초과..
# 이중 for문을 돌리면 안됨..