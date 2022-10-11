from copy import deepcopy
from itertools import permutations as pp
import sys
input = sys.stdin.readline


def turn(order):
    di = [0, 1, 0, -1]     # 우, 하, 좌, 상
    dj = [1, 0, -1, 0]
    ar = deepcopy(arr)
    for i in order:
        x1, y1 = turn_info[i][0]
        x2, y2 = turn_info[i][1]
        h = 0
        x, y, before = x1, y1, ar[x1][y1]
        while True:
            if x1 >= x2 or y1 >= y2:
                break
            nx, ny = x + di[h], y + dj[h]
            if x1 <= nx <= x2 and y1 <= ny <= y2:
                temp = ar[nx][ny]
                ar[nx][ny] = before
                before = temp
                x, y = nx, ny
            else:
                h += 1

            if h == 4:
                x, y = x1 + 1, y1 + 1
                h = 0
                x1, y1, x2, y2 = x1 + 1, y1 + 1, x2 - 1, y2 - 1
                before = ar[x1][y1]

    return ar


N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn_info = []
for _ in range(k):
    r, c, s = map(int, input().split())
    turn_info.append([(r-s-1, c-s-1), (r+s-1, c+s-1)])

result = 10**9
for p in pp(range(k), k):
    a = turn(p)
    min_sum = min([sum(i) for i in a])
    result = min(result, min_sum)

print(result)