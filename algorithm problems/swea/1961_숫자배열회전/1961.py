import sys
sys.stdin = open('input.txt')

T = int(input())


def turn_90(ar, n):
    turned_ar = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turned_ar[j][n-1-i] = ar[i][j]
    return turned_ar



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*3 for _ in range(N)]

    turned = turn_90(arr, N)
    for i in range(N):
        line = ''
        for j in range(N):
            line += str(turned[i][j])
        result[i][0] = line

    turned = turn_90(turned, N)
    for i in range(N):
        line = ''
        for j in range(N):
            line += str(turned[i][j])
        result[i][1] = line

    turned = turn_90(turned, N)
    for i in range(N):
        line = ''
        for j in range(N):
            line += str(turned[i][j])
        result[i][2] = line

    print(f'#{tc}')
    for i in range(N):
        print(*result[i])