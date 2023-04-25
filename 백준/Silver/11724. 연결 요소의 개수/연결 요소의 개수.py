import sys
input = sys.stdin.readline

N, M = map(int, input().split())
info = {}
for _ in range(M):
    a, b = map(int, input().split())
    if (a - 1) not in info.keys():
        info[a - 1] = [b - 1]
    else:
        info[a - 1].append(b - 1)
    if (b - 1) not in info.keys():
        info[b - 1] = [a - 1]
    else:
        info[b - 1].append(a - 1)

result = 0
visited = [0] * N
while visited.count(0) != 0:
    s = [visited.index(0)]
    result += 1
    while s:
        p = s.pop()
        if visited[p]:
            continue
        else:
            visited[p] = 1
            if p in info.keys():
                for n in info[p]:
                    if not visited[n]:
                        s.append(n)

print(result)