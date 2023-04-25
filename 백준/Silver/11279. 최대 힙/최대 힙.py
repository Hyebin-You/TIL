import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    n = int(input())
    if n:
        heappush(arr, -n)
    else:   # n 이 0 인 경우
        if len(arr):   # 배열이 비어있지 않으면
            a = heappop(arr)
            print(-a)
        else:       # 배열이 비어있다면
            print(0)