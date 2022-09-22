import sys
from copy import deepcopy
sys.stdin = open('sample_input.txt')


def drop_ball(arr, y):
    di = [-1, 1, 0, 0]         # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]

    stack = []
    for i in range(H):          # 첫 충돌지점 찾기
        if arr[i][y]:
            stack.append((i, y))
            break

    remove = []
    while stack:
        a, b = stack.pop()
        remove.append((a, b))
        w = arr[a][b]
        arr[a][b] = 0
        for i in range(1, w):
            for h in range(4):
                nx, ny = a + di[h]*i, b + dj[h]*i
                if 0 <= nx < H and 0 <= ny < W and arr[nx][ny]:
                    if (nx, ny) not in stack:
                        stack.append((nx, ny))

    for line in arr:
        if line.count(0) != len(line):
            break
    else:
        return len(remove)

    HxW = [[0] * H for _ in range(W)]  # arr의 전치행렬
    for i in range(H):
        for j in range(W):
            HxW[j][i] = arr[i][j]

    for i in range(W):
        z_cnt = HxW[i].count(0)
        n_l = [0] * z_cnt
        for j in range(H):
            if HxW[i][j]:
                n_l.append(HxW[i][j])
        HxW[i] = n_l

    for i in range(H):
        for j in range(W):
            arr[i][j] = HxW[j][i]

    return len(remove)


def DFS(y, arr, time):
    global result
    board = deepcopy(arr)
    c = drop_ball(board, y)
    stack = [(c, board, time + 1)]
    while stack:
        c, board, t = stack.pop()
        if c == num_blocks:
            result = c
            break
        for i in range(W):
            b = deepcopy(board)
            cc = drop_ball(b, i)
            if t + 1 == N:
                if result < c + cc:
                    result = c + cc
            else:
                stack.append((c+cc, b, t + 1))


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    num_blocks = W*H - sum(i.count(0) for i in blocks)

    result = 0
    for k in range(W):
        DFS(k, blocks, 0)

    print(f'#{tc} {num_blocks - result}')