import sys

sys.stdin = open('input.txt')


def ways(ladder, i, j):
    di = [1, 0, 0]  # 하, 좌, 우
    dj = [0, -1, 1]
    N = 100
    now_h = 0

    if ladder[i][j] == 0:
        return -1

    while True:
        able_pos = [0, 0, 0]
        for h in range(3):
            if (0 <= i + di[h] < N and 0 <= j + dj[h] < N) and ladder[i + di[h]][j + dj[h]] == 1:
                able_pos[h] = 1
        if able_pos[1] == able_pos[2] == 0:
            i += di[0]
            j += dj[0]
        elif able_pos[0] == 1 and (able_pos[1] == 1 or able_pos[2] == 1):
            if now_h == 0:
                if able_pos[1] == 1:
                    i += di[1]
                    j += dj[1]
                    now_h = 1
                else:
                    i += di[2]
                    j += dj[2]
                    now_h = 2
            else:
                i += di[0]
                j += dj[0]
                now_h = 0
        else:
            i += di[now_h]
            j += dj[now_h]

        if i == 99:
            break

    return j


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for k in range(100):
        j_index = ways(arr, 0, k)
        if j_index == -1:
            continue
        if arr[99][j_index] == 2:
            break

    print(f'#{tc} {k}')