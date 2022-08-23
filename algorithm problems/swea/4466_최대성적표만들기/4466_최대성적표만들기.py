import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort(reverse=True)
    total = 0
    for i in range(K):
        total += scores[i]

    print(f'#{tc} {total}')