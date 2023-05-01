import sys
from collections import deque
input = sys.stdin.readline



# M은 j, N은 i
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
while q:
    x, y = q.popleft()
    for h in range(4):
        nx, ny = x + di[h], y + dj[h]
        if 0 <= nx < N and 0 <= ny < M and not box[nx][ny]:
            box[nx][ny] = box[x][y] + 1
            q.append((nx, ny))

result = 0

for l in box:
    if 0 in l:
        print(-1)
        break
    else:
        result = max(result, max(l))
else:
    print(result - 1)