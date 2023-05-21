import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = {}
for _ in range(n):
    a, b = input().split()
    info[a] = b

for _ in range(m):
    print(info[input().rstrip()])