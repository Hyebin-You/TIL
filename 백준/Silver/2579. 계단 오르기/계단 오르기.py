import sys
input = sys.stdin.readline

N = int(input())
stair = [int(input()) for _ in range(N)]

if N > 3:
    res = [stair[0]]
    res.append(stair[0] + stair[1])
    res.append(max(stair[2] + stair[1], stair[0] + stair[2]))

    for i in range(3, N):
        res.append(max(stair[i] + stair[i-1] + res[i - 3], stair[i] + res[i-2]))

    print(res[-1])
else:
    res = [stair[0]]
    if N == 2:
        res.append(stair[0] + stair[1])
    elif N == 3:
        res.append(stair[0] + stair[1])
        res.append(max(stair[2] + stair[1], stair[0] + stair[2]))
    print(res[-1])