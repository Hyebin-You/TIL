import sys
sys.stdin = open('sample_input.txt')


def make_num(x, y, word):
    global result
    di = [-1, 1, 0, 0]         # 상 하 좌 우
    dj = [0, 0, -1, 1]

    if len(word) == 7:
        result.add(word)
        return

    for i in range(4):
        if 0 <= x + di[i] < 4 and 0 <= y + dj[i] < 4:
            make_num(x + di[i], y + dj[i], word + str(board[x][y]))


T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(4)]

    result = set()
    for i in range(4):
        for j in range(4):
            make_num(i, j, '')

    print(f'#{tc} {len(result)}')