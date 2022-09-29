import sys
sys.stdin = open('sample_input.txt')


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
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    info.sort(key= lambda x:x[2])
    p = [i for i in range(V+1)]

    cnt = 0
    result = 0
    for i in info:
        if findset(i[0]) != findset(i[1]):
            cnt += 1
            result += i[2]
            union(i[0], i[1])
        if cnt == V:
            break

    print(f'#{tc} {result}')