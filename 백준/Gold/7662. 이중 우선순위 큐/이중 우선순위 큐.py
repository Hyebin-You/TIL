import sys
from heapq import heappop, heappush
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())

    q1 = []
    q2 = []
    visited = [0] * k

    for i in range(k):
        c, n = input().split()
        if c == 'I':
            heappush(q1, (int(n), i))
            heappush(q2, (-int(n), i))
            visited[i] = 1
        else:
            if n == '-1':
                while q1 and not visited[q1[0][1]]:
                    heappop(q1)
                if q1:
                    visited[q1[0][1]] = 0
                    heappop(q1)
            else:
                while q2 and not visited[q2[0][1]]:
                    heappop(q2)
                if q2:
                    visited[q2[0][1]] = 0
                    heappop(q2)

    while q1 and not visited[q1[0][1]]:
        heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heappop(q2)

    if not q1:
        print('EMPTY')
    else:
        print(-q2[0][0], q1[0][0])
