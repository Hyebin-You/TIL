import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

total = 0
stack = [(1, 0)]
visited = [0] * (N + 1)
# visited = []로 해놓고 방문할때 append하면 시간초과 발생
while stack:
    s, cnt = stack.pop()
    visited[s] = 1
    if s != 0 and len(tree[s]) == 1:
        total += cnt

    for n in tree[s]:
        if not visited[n]:
            stack.append((n, cnt + 1))

if total%2:
    print('Yes')
else:
    print('No')