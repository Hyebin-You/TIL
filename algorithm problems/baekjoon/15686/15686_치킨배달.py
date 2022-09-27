import sys
from itertools import combinations as comb
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

h_pos = []
c_pos = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            h_pos.append((i, j))
        elif arr[i][j] == 2:
            c_pos.append((i, j))

result = 10**6
c_list = list(comb(c_pos, M))

for cc in c_list:
    total = 0
    for h in h_pos:
        d = 10**6
        for c in cc:
            if d > abs(c[0] - h[0]) + abs(c[1] - h[1]):
                d = abs(c[0] - h[0]) + abs(c[1] - h[1])
        total += d
        if total > result:
            break
    else:
        if result > total:
            result = total

print(result)