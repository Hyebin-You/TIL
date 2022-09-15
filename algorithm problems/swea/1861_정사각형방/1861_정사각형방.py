import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]         # 상 하 좌 우
    dj = [0, 0, -1, 1]

    length = 0
    result = 0
    for i in range(N):
        for j in range(N):
            visited = [(i, j)]
            x, y = i, j
            while True:
                for h in range(4):
                    nx = x + di[h]
                    ny = y + dj[h]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == arr[x][y] + 1:
                            visited.append((nx, ny))
                            x, y = nx, ny
                            break
                else:
                    break
            if len(visited) > length:
                length = len(visited)
                result = arr[i][j]
            elif len(visited) == length:
                if result > arr[i][j]:
                    result = arr[i][j]

    print(f'#{tc} {result} {length}')