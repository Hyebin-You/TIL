import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
info = {}

for _ in range(N + M):
    a, b = map(int, input().split())
    info[a] = b

visited = [0] * 101
q = deque([1])
while q:
    pos = q.popleft()

    for i in range(6, 0, -1):
        npos = pos + i
        if npos > 100:
            continue
        if npos in info.keys():
            npos = info[npos]
        if visited[npos]:
            if visited[npos] > visited[pos] + 1:
                visited[npos] = visited[pos] + 1
                q.append(npos)
        else:
            visited[npos] = visited[pos] + 1
            q.append(npos)

print(visited[100])