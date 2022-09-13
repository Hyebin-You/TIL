import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def find_cnt(root):
    global visited, cnt
    cnt[root] = 1
    visited[root] = True
    for i in info[root]:
        if not visited[i]:
            find_cnt(i)
            cnt[root] += cnt[i]
    return


N, R, Q = map(int, input().split())
info = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    info[u].append(v)
    info[v].append(u)

visited = [False] * (N + 1)
cnt = [0] * (N + 1)

find_cnt(R)

for _ in range(Q):
    root = int(input())
    print(cnt[root])