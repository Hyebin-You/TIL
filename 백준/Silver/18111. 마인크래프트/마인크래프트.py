import sys
input = sys.stdin.readline


def check_time(ar, h, n_block):
    work1 = 0
    work2 = 0
    for i in range(N):
        for j in range(M):
            if ar[i][j] < h:
                work2 += h - ar[i][j]
            elif ar[i][j] > h:
                work1 += ar[i][j] - h

    if work1 + n_block >= work2:
        return work1 * 2 + work2
    else:
        return -1


N, M, B = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
mh, nh = 0, 256
for a in area:
    mh = max(mh, max(a))
    nh = min(nh, min(a))

result = 500 * 500 * 2 * 256
result_h = 0
for h in range(nh, mh + 1):
    t = check_time(area, h, B)
    if t != -1:
        if result > t:
            result = t
            result_h = h
        elif result == t:
            result_h = max(result_h, h)

print(result, result_h)