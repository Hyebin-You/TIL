import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
pri_q = []
plus = {}
minus = {}

for _ in range(N):
    x = int(input())

    if not x:
        if len(pri_q):
            n = heappop(pri_q)
            if -n not in minus.keys() or not minus[-n]:
                plus[n] -= 1
                print(n)
            else:
                minus[-n] -= 1
                print(-n)
        else:
            print(0)
    else:
        if x > 0:
            heappush(pri_q, x)
            if x in plus.keys():
                plus[x] += 1
            else:
                plus[x] = 1
        else:
            heappush(pri_q, -x)
            if x in minus.keys():
                minus[x] += 1
            else:
                minus[x] = 1