import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [-1, 1, 0, 0]      # 상 하 좌 우
    dj = [0, 0, -1, 1]

    d = [[10**8] * (N) for _ in range(N)]
    d[0][0] = 0
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop(0)
        for h in range(4):
            nx, ny = x + di[h], y + dj[h]
            if 0 <= nx < N and 0 <= ny < N and d[x][y] + int(arr[nx][ny]) < d[nx][ny]:
                d[nx][ny] = d[x][y] + int(arr[nx][ny])
                stack.append((nx, ny))

    print(f'#{tc} {d[N-1][N-1]}')