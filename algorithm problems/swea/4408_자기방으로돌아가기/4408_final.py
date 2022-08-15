import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * 200

    for i in range(N):
        for j in range(2):
            if arr[i][j] % 2:
                arr[i][j] = (arr[i][j] + 1) // 2
            else:
                arr[i][j] //= 2

    print(arr)

    for ways in arr:
        for k in range(min(ways) - 1, max(ways)):
            p[k] += 1

    print(f'#{tc} {max(p)}')