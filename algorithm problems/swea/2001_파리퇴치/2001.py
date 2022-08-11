import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            subset_sum = 0
            for r in range(M):
                for c in range(M):
                    subset_sum += arr[i+r][j+c]
            if max_sum < subset_sum:
                max_sum = subset_sum

    print(f'#{tc} {max_sum}')