import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    info = {}

    n = int(input())
    for i in range(n):
        a, b = input().split()
        if b in info.keys():
            info[b] += 1
        else:
            info[b] = 1

    result = 1
    for v in info.values():
        result *= v + 1

    print(result - 1)