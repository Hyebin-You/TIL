import sys
input = sys.stdin.readline

def check(a, b):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    cnt = 0
    s = [(a, b)]
    while s:
        x, y = s.pop()
        if arr[x][y] == "1":
            arr[x][y] = 0
            cnt += 1

            for h in range(4):
                nx, ny = x + di[h], y + dj[h]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == "1":
                        s.append((nx, ny))

    return cnt


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
r_cnt = 0
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == "1":
            r_cnt += 1
            result.append(check(i, j))

result.sort()
print(r_cnt)
for n in result:
    print(n)