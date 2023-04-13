import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

if min(heights) > M:
    start = min(heights) - M
else:
    start = 1
end = max(heights) - 1
result = 0

while start <= end:
    mid = (start + end) // 2
    cutting = 0
    for h in heights:
        if h >= mid:
            cutting += h - mid

    if cutting >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)