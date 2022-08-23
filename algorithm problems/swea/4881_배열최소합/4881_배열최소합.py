import sys
sys.stdin = open('sample_input.txt')


def choose_num(idx_row, n, total):
    global min_sum
    global col
    if total > min_sum:
        return

    if idx_row == n:
        if total < min_sum:
            min_sum = total
        return
    else:
        for i in range(N):
            if not col[i]:
                col[i] = 1
                choose_num(idx_row+1, n, total + arr[idx_row][i])
                col[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [0] * N
    min_sum = 100

    choose_num(0, N, 0)
    print(f'#{tc} {min_sum}')