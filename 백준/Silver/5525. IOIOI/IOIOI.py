import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

p = 'I'
for _ in range(N):
    p += 'OI'

l = len(p)

result = 0
for i in range(M - N):
    test = S[i:i+l]
    if test == p:
        result += 1

print(result)