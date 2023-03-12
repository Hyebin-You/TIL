from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
t = 0
result = []
while q:
    p = q.popleft()
    t += 1
    if t == k:
        result.append(str(p))
        t = 0
    else:
        q.append(str(p))

print('<' + ', '.join(result) + '>')