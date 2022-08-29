import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(M)]
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = 'W'
    board[N//2-1][N//2] = 'B'
    board[N//2][N//2-1] = 'B'
    board[N//2][N//2] = 'W'

    di = [-1, 1, 0, 0, -1, 1, -1, 1]         # 상하좌우 좌상 좌하 우상 우하
    dj = [0, 0, -1, 1, -1, -1, 1, 1]
    for stone in info:
        x, y = stone[1] - 1, stone[0] - 1
        if stone[2] == 1:
            board[x][y] = 'B'
        else:
            board[x][y] = 'W'
        for d in range(8):
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] and board[x][y] != board[nx][ny]:
                    stack = [(nx, ny)]
                    i = 1
                    while True:
                        nnx = nx + di[d] * i
                        nny = ny + dj[d] * i
                        if 0 <= nnx < N and 0 <= nny < N:
                            if board[nnx][nny] == board[nx][ny]:
                                stack.append((nnx, nny))
                                i += 1
                            elif board[nnx][nny] == board[x][y]:
                                for _ in range(len(stack)):
                                    a, b = stack.pop()
                                    board[a][b] = board[x][y]
                                break
                            else:
                                break
                        else:
                            break

    b_cnt = 0
    w_cnt = 0
    for line in board:
        b_cnt += line.count('B')
        w_cnt += line.count('W')

    print(f'#{tc}', b_cnt, w_cnt)