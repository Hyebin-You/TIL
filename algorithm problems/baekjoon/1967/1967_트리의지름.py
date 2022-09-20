import sys
input = sys.stdin.readline


def bfs(start):
    q = [(start, 0)]
    visited = []
    result = 0
    num_node = 0
    while q:
        s, w = q.pop(0)
        visited.append(s)
        n_cnt = 0
        for j in tree[s]:
            if j[0] not in visited:
                q.append((j[0], w + j[1]))
            else:
                n_cnt += 1
        if n_cnt == len(tree[s]):
            if result < w:
                result = w
                num_node = s

    return num_node, result

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

s = bfs(1)
e, w = bfs(s[0])
print(w)