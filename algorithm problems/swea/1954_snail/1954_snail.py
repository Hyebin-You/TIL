import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    num = 1
    di = [0, 1, 0, -1] # 우 하 좌 상
    dj = [1, 0, -1, 0]
    i = j = d = 0

    while True:
        if (0 <= i+di[d] < N and 0 <= j+dj[d] < N) and arr[i+di[d]][j+dj[d]] == 0:
            arr[i][j] = num
            i += di[d]
            j += dj[d]
            num += 1
        else:
            arr[i][j] = num
            d = (d+1)%4

        if N == 1 or num == N**2:
            arr[i][j] = num
            break

    print(f'#{tc}')
    for i in arr:
        print(*i)