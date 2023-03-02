from collections import deque

N = int(input())
q = deque([i for i in range(1, N+1)])


while len(q) != 1:
    q.popleft()
    if len(q) == 1:
        break
    q.append(q.popleft())
    if len(q) == 1:
        break

print(q[0])