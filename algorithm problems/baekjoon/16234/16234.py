import sys
input = sys.stdin.readline


def open_country(ar, a, b):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    near_c = [(a, b)]
    q = [(a, b)]
    while q:
        x, y = q.pop()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        for h in range(4):
            nx, ny = x + di[h], y + dj[h]
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(ar[nx][ny] - ar[x][y]) <= r:
                    q.append((nx, ny))
                    if (nx, ny) not in near_c:
                        near_c.append((nx, ny))

    return near_c


n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]

day = 0
while True:
    visited = [[0] * n for _ in range(n)]
    near = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                rc = open_country(country, i, j)
                if len(rc) > 1:
                    near.append(rc)

    if len(near):
        for u in near:
            s = sum([country[k[0]][k[1]] for k in u])
            for c in u:
                country[c[0]][c[1]] = s // len(u)
        day += 1
    else:
        break

print(day)