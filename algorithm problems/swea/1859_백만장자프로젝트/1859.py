import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_idx = N-1

    for i in range(N-1, -1, -1):
        if arr[i] < arr[max_idx] and i < max_idx:
            result += arr[max_idx] - arr[i]
        elif arr[i] > arr[max_idx]:
            max_idx = i

    print(f'#{tc} {result}')


# 어디서부터 탐색하느냐 로 코드길이가 많이 달라질 수 있는 문제
# 탐색위치 고려하기