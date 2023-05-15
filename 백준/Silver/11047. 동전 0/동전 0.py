import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = [0] * n
for i in range(n-1, -1, -1):
    A[i] = int(input())

result = 0
for a in A:
    result += k // a
    k -= (k // a) * a

print(result)