import sys
input = sys.stdin.readline

N = int(input())
t = int(input())
info = {}
for _ in range(t):
    a, b = map(int, input().split())
    if a in info.keys():
        info[a].append(b)
    else:
        info[a] = [b]
    if b in info.keys():
        info[b].append(a)
    else:
        info[b] = [a]

stack = [1]
result = [0] * (N + 1)
while stack:
    s = stack.pop()
    if result[s]:   # 방문했다면
        continue

    result[s] = 1
    for l in info[s]:
        stack.append(l)

print(result.count(1) - 1)