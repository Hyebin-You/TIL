import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [0] * (N + 1)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                count_row = 1
                count_col = 1
                h = 1
                while True:
                    if j == 0 or arr[i][j - 1] == 0:
                        if j + h < N and arr[i][j + h] == 1:
                            count_row += 1
                            h += 1
                        else:
                            break
                    else:
                        break

                result[count_row] += 1

                h = 1
                while True:
                    if i == 0 or arr[i - 1][j] == 0:
                        if i + h < N and arr[i + h][j] == 1:
                            count_col += 1
                            h += 1
                        else:
                            break
                    else:
                        break

                result[count_col] += 1

    print(f'#{tc} {result[K]}')