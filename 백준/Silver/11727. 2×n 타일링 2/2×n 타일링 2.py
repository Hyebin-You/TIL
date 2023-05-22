import sys
input = sys.stdin.readline

n = int(input())
info = [0] * (n + 1)

if n == 1:
    print(1)
else:
    info[1] = 1
    info[2] = 3
    i = 3
    while i <= n:
        info[i] = info[i-1] + info[i-2] * 2
        i += 1

    print(info[n] % 10007)