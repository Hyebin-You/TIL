import sys
sys.stdin = open('sample_input.txt')


def find_dist(x,  y, arr):
    di = [-1, 1, 0, 0]         # 상 하 좌 우
    dj = [0, 0, -1, 1]
    visited = []
    q = [(x, y, 0)]

    while q:
        t = q.pop(0)
        visited.append((t[0], t[1]))

        for i in range(4):
            if 0 <= t[0] + di[i] < len(arr) and 0 <= t[1] + dj[i] < len(arr):
                if arr[t[0] + di[i]][t[1] + dj[i]] == '0' and (t[0] + di[i], t[1] + dj[i]) not in visited:
                    q.append((t[0] + di[i], t[1] + dj[i], t[2] + 1))
                elif arr[t[0] + di[i]][t[1] + dj[i]] == '3':
                    return t[2]

    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                x, y = i, j

    print(f'#{tc} {find_dist(x, y, maze)}')