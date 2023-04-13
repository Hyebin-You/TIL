import sys
input = sys.stdin.readline


def check_length(length):
    result = 0
    for l in lines:
        result += l // length

    if result >= N:
        return True
    else:
        return False


K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)
answer = 0
while start <= end:
    mid = (start + end) // 2

    if check_length(mid):
        start = mid + 1
        answer = mid
    else:
        end = mid - 1


print(answer)