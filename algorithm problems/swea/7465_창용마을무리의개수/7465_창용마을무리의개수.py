import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    result = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            q = [i]
            while q:
                n = q.pop(0)
                if not visited[n]:
                    visited[n] = 1
                    for j in range(1, N+1):
                        if arr[n][j] and not visited[j]:
                            q.append(j)
            result += 1

    print(f'#{tc} {result}')