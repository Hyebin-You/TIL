import sys
sys.stdin = open('input.txt')


def find_way(x, y):            # x, y : 시작점의 좌표
    global maze
    di = [-1, 1, 0, 0]                    # 상 하 좌 우
    dj = [0, 0, -1, 1]
    q = [(x, y)]

    while q:
        t = q.pop(0)
        maze[t[0]][t[1]] = -1
        for i in range(4):
            if 0 <= t[0] + di[i] < 16 and 0 <= t[1] + dj[i] < 16:
                if maze[t[0] + di[i]][t[1] + dj[i]] == '0':
                    q.append((t[0] + di[i], t[1] + dj[i]))
                elif maze[t[0] + di[i]][t[1] + dj[i]] == '3':
                    return 1

    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(input()) for i in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                x, y = i, j
                break

    print(f'#{tc} {find_way(x, y)}')