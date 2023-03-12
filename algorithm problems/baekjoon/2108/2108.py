import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
c = Counter(nums)
nn = []
for k, v in c.items():
    if v == max(c.values()):
        nn.append(k)

print(round(sum(nums)/n))
print(nums[n//2])
if len(nn) > 1:
    print(nn[1])
else:
    print(nn[0])
print(max(nums) - min(nums))