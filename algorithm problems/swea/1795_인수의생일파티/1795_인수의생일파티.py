import sys
sys.stdin = open('input.txt')


def each_to_start(start):
    q = [start]
    while q:
        n = q.pop(0)
        for i in range(1, N+1):
            if i == start:
                continue
            if arr[i][n]:
                if not each_D[i] or each_D[i] > each_D[n] + arr[i][n]:
                    each_D[i] = each_D[n] + arr[i][n]
                    q.append(i)


def start_to_each(start):
    q = [start]
    while q:
        n = q.pop(0)
        for i in range(1, N+1):
            if i == start:
                continue
            if arr[n][i]:
                if not start_D[i] or start_D[i] > start_D[n] + arr[n][i]:
                    start_D[i] = start_D[n] + arr[n][i]
                    q.append(i)


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        arr[x][y] = c

    start_D = [0] * (N+1)
    start_to_each(X)

    each_D = [0] * (N+1)
    each_to_start(X)
    result = max([each_D[i] + start_D[i] for i in range(1, N+1)])
    print(f'#{tc} {result}')