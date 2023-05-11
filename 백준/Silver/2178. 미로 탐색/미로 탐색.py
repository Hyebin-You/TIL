import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

q = deque([])
q.append((0, 0))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
while q:
    x, y = q.popleft()

    for h in range(4):
        nx, ny = x + di[h], y + dj[h]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == '1':
                arr[nx][ny] = int(arr[x][y]) + 1
                q.append((nx, ny))

print(arr[N-1][M-1])