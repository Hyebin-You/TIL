import sys
input = sys.stdin.readline


def min_len(idx, length, start, end):
    global result, shortcut

    if idx == len(shortcut):
        length += end - start
        if length < result:
            result = length
        return

    way = shortcut[idx]
    if way[0] >= start:
        min_len(idx + 1, length, start, end)
        length += way[0] - start + way[2]
        start = way[1]
        min_len(idx + 1, length, start, end)
    else:
        min_len(idx + 1, length, start, end)


N, D = map(int, input().split())
shortcut = []
for _ in range(N):
    info = list(map(int, input().split()))
    if info[2] < info[1] - info[0]:
        if info[1] <= D:
            shortcut.append(info)

shortcut.sort(key=lambda x: x[0])
result = D
min_len(0, 0, 0, D)

print(result)