from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

info = Counter(cards)

for n in nums:
    if n in info:
        print(info[n], end=' ')
    else:
        print(0, end=' ')