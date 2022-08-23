import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    for i in range(abs(N - M) + 1):
        sub_sum = 0
        for j in range(min(N,M)):
            if N < M:
                sub_sum += A[j] * B[i + j]
            else:
                sub_sum += A[i+j] * B[j]
        if sub_sum > result:
            result = sub_sum

    print(f'#{tc} {result}')