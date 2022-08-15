import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda i: i[0])
arr.sort(key=lambda i: i[1])
last = arr[0]
result = 1
for i in range(1, N):
    if arr[i][0] >= last[1]:
        result += 1
        last = arr[i]

print(result)