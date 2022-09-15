import sys
sys.stdin = open('input.txt')


def find_height(idx, total):
    global result

    if total - B > result:
        return
    if idx == N:
        if total >= B:
            if total - B < result:
                result = total - B
        return

    find_height(idx + 1, total)
    find_height(idx + 1, total + height[idx])


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    result = B
    find_height(0, 0)
    print(f'#{tc} {result}')