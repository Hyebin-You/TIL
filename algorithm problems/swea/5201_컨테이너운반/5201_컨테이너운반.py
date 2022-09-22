import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    T = list(map(int, input().split()))

    weight.sort(reverse=True)
    T.sort(reverse=True)
    if T[0] < weight[N-1]:
        print(f'#{tc} {0}')
        continue

    total = 0
    for i in range(M):
        for j in range(N):
            if 0 < weight[j] <= T[i]:
                total += weight[j]
                weight[j] = -1
                break

    print(f'#{tc} {total}')