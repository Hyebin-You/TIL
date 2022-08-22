import sys
import math
input = sys.stdin.readline

N, S = map(int, input().split())
pos = list(map(int, input().split()))

for i in range(N):
    pos[i] = abs(pos[i] - S)

print(math.gcd(*pos))


## 최대공약수를 구하는 문제