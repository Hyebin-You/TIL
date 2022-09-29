import sys
sys.stdin = open('re_sample_input.txt')


def findset(x):
    if p[x] != x:
        p[x] = findset(p[x])
    return p[x]


def union(x, y):
    a, b = findset(x), findset(y)
    if a > b:
        p[b] = a
    else:
        p[a] = b


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_pos = list(map(int, input().split()))
    y_pos = list(map(int, input().split()))
    E = float(input())

    p = [i for i in range(N)]
    island = []
    for i in range(N):
        island.append((x_pos[i], y_pos[i]))

    line = []
    for i in range(N):
        for j in range(i+1, N):
            w = E * (abs(island[i][0] - island[j][0]) ** 2 + abs(island[i][1] - island[j][1]) ** 2)
            line.append((i, j, w))

    result = 0
    cnt = 0
    line.sort(key= lambda x: x[2])
    for l in line:
        if findset(l[0]) != findset(l[1]):
            result += l[2]
            cnt += 1
            union(l[0], l[1])
        if cnt == N-1:
            break

    print(f'#{tc} {round(result)}')