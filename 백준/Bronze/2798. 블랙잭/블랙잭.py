from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
for comb in combinations(nums, 3):
    s = sum(comb)
    if s <= M:
        result = max(result, s)

print(result)