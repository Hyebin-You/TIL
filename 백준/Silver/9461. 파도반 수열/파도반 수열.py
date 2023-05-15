import sys
input = sys.stdin.readline

T = int(input())
p = [1, 1, 1, 2, 2, 3, 4, 5, 7]
for _ in range(T):
    N = int(input())

    if len(p) >= N:
        print(p[N-1])
    else:
        while len(p) < N:
            p.append(p[-1] + p[-5])
        print(p[-1])