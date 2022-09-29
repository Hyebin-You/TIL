import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[0] * N for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for h in range(4):
            nx, ny = x + di[h], y + dj[h]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > arr[x][y]:
                    d = 1 + arr[nx][ny] - arr[x][y]
                else:
                    d = 1
                if not D[nx][ny] or D[nx][ny] > D[x][y] + d:
                    D[nx][ny] = D[x][y] + d
                    q.append((nx, ny))

    print(f'#{tc} {D[-1][-1]}')