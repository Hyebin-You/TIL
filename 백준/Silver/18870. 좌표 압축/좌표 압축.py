import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
b = sorted(list(set(nums)))

info = {b[i]: i for i in range(len(b))}
result = [info[n] for n in nums]
print(*result)