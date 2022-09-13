import sys
input = sys.stdin.readline

n = int(input())
box_info = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if box_info[i] > box_info[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))