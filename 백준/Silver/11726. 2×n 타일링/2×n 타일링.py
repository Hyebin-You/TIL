import sys
input = sys.stdin.readline

n = int(input())

nums = [0] * 1001
nums[1] = 1
nums[2] = 2
s = 3
while s <= n:
    nums[s] = nums[s-1] + nums[s-2]
    s += 1

print(nums[n] % 10007)