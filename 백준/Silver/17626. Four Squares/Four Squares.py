import sys
input = sys.stdin.readline

n = int(input())
dp = [10**9] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    for j in range(1, int(n ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i-j**2] + 1)

print(dp[n])