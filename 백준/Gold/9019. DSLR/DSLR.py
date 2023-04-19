import sys
from collections import deque
input = sys.stdin.readline


def command(nn, cm):
    if cm == 'D':
        nn *= 2
        if nn > 9999:
            nn %= 10000
        return nn
    elif cm == 'S':
        if nn:
            return nn-1
        else:
            return 9999
    else:
        nn = str(nn)
        for i in range(4 - len(nn)):
            nn = '0' + nn
        if cm == 'L':
            return int(nn[1:] + nn[0])
        else:
            return int(nn[3] + nn[0:3])


T = int(input())
co = ['D', 'S', 'L', 'R']
for _ in range(T):
    A, B = map(int, input().split())
    num = [''] * 10000

    q = deque([A])
    while q:
        n = q.popleft()

        if n == B:
            continue
        if num[B] != '' and len(num[n]) >= len(num[B]):
            continue

        for c in co:
            nc = command(n, c)
            if nc == n:
                continue
            # 이미 방문한 곳이면
            if num[nc] != '':
                if len(num[nc]) > len(num[n]) + 1:
                    # 갱신이 필요하다면
                    num[nc] = num[n] + c
                    q.append(nc)
            # 방문한 적이 없으면
            else:
                num[nc] = num[n] + c
                q.append(nc)

    print(num[B])