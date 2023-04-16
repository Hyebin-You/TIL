import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    n = int(input())

    if n:
        heappush(nums, n)
    else:
        if len(nums):
            print(heappop(nums))
        else:
            print(0)