import sys
sys.stdin = open('in1.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0, -1, 1, -1, 1]        # 상 하 좌 우 좌상 좌하 우상 우하
    dj = [0, 0, -1, 1, -1, -1, 1, 1]


    result = 0
    for i in range(N):
        for j in range(N):
            cnt_T = arr[i][j]
            cnt_X = arr[i][j]
            for k in range(1, M):
                for h in range(4):  # 상 하 좌 우 확인
                    nx = i + di[h] * k
                    ny = j + dj[h] * k
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt_T += arr[nx][ny]
            for k in range(1, M):
                for h in range(4, 8):  # 좌상 좌하 우상 우하 확인
                    nx = i + di[h] * k
                    ny = j + dj[h] * k
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt_X += arr[nx][ny]
            if result < max(cnt_T, cnt_X):
                result = max(cnt_T, cnt_X)

    print(f'#{tc} {result}')