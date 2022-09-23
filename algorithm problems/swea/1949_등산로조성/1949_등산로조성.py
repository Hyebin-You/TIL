import sys
sys.stdin = open('sample_input.txt')


def BFS(start):
    global result
    di = [-1, 1, 0, 0]         # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]

    x, y = start
    q = [(x, y, arr[x][y], 0, 1, [(x, y)])]          # x, y, 높이, 깎은 횟수, 길이
    while q:
        x, y, h, t, l, visited = q.pop(0)
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            cnt = 0
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] < h:
                    v = visited.copy()
                    v.append((nx, ny))
                    q.append((nx, ny, arr[nx][ny], t, l+1, v))
                    cnt += 1
                else:
                    if t != 1:
                        for i in range(1, K + 1):
                            if arr[nx][ny] - i < h and (nx, ny) not in visited:
                                v = visited.copy()
                                v.append((nx, ny))
                                q.append((nx, ny, arr[nx][ny] - i, t + 1, l+1, v))
                                cnt += 1
        if not cnt:             # 더 이상 이 점 주변으로 이동할 수 없을 때
            if t < 2:
                if result < l:
                    result = l


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    max_h = max([max(i) for i in arr])
    for a in range(N):
        for b in range(N):
            if arr[a][b] == max_h:
                BFS((a, b))

    print(f'#{tc} {result}')