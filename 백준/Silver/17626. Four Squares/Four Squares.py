import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    min_V = 10**9
    for j in range(1, int(i ** 0.5) + 1):
        min_V = min(min_V, dp[i-j**2])
    dp[i] = min_V + 1

print(dp[n])