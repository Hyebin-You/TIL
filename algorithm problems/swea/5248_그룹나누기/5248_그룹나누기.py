import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))

    arr = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(M):
        a, b = info[i*2], info[i*2+1]
        arr[a][b] = 1
        arr[b][a] = 1

    result = 0
    for i in range(1, N+1):
        if not visited[i]:
            g = [i]
            while g:
                n = g.pop()
                if not visited[n]:
                    visited[n] = 1
                    for j in range(1, N+1):
                        if arr[n][j] and not visited[j]:
                            g.append(j)
            result += 1

    print(f'#{tc} {result}')