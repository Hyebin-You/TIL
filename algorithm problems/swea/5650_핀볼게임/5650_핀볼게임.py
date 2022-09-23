import sys
sys.stdin = open('sample_input.txt')


def start_game(x, y, h):
    di = [-1, 1, 0, 0]                 # 상 0 , 하 1, 좌 2, 우 3
    dj = [0, 0, -1, 1]
    turn_d = {1: [(1, 3), (2, 0)], 2: [(0, 3), (2, 1)], 3: [(3, 1), (0, 2)], 4: [(3, 0), (1, 2)]}
    g_b = {0: 1, 1: 0, 2: 3, 3: 2}

    start = (x, y)
    cnt = 0
    while True:
        if 0 <= x + di[h] < N and 0 <= y + dj[h] < N:
            x, y = x + di[h], y + dj[h]
        else:               # 벽에 부딪혔을때
            cnt += 1
            h = g_b[h]

        if (x, y) == start:             # 출발지점으로 돌아왔을때
            return cnt

        if board[x][y] == 5:            # 블록에 부딪혔을때
            cnt += 1
            h = g_b[h]
        elif board[x][y] in [1, 2, 3, 4]:       # 삼각블록에 부딪혔을때
            h_list = turn_d[board[x][y]]
            cnt += 1
            if h == h_list[0][0]:
                h = h_list[0][1]
            elif h == h_list[1][0]:
                h = h_list[1][1]
            else:
                h = g_b[h]
        elif board[x][y] in [6, 7, 8, 9, 10]:       # 웜홀에 도착했을때
            w_pos = w_h[board[x][y]]
            if (x, y) == w_pos[0]:
                x, y = w_pos[1]
            else:
                x, y = w_pos[0]
        elif board[x][y] == -1:         # 블랙홀에 도달했을때
            return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    w_h = {6: [], 7: [], 8: [], 9: [], 10: []}
    for i in range(N):
        for j in range(N):
            if board[i][j] in [6, 7, 8, 9, 10]:
                w_h[board[i][j]].append((i, j))

    result = 0
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                for k in range(4):
                    score = start_game(i, j, k)
                    if result < score:
                        result = score

    print(f'#{tc} {result}')