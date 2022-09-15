import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 1, -1]     # 우상, 우하, 좌하, 좌상
    dj = [1, 1, -1, -1]
    result = 0

    for i in range(N):
        for j in range(N):
            able_info = []
            now_b = 1
            while True:             # 현 좌표에서 우하로 내려갈 수 있는 횟수
                if 0 <= i + di[1] * now_b < N and 0 <= j + dj[1] * now_b < N:
                    now_b += 1
                else:
                    now_b -= 1
                    break

            a = 1
            while True:
                nx = i + di[0]*a
                ny = j + dj[0]*a
                if 0 <= nx < N and 0 <= ny < N:       # 우상 방향
                    b = 1
                    while True:
                        if 0 <= nx + di[1]*b < N and 0 <= ny + dj[1]*b < N:
                            b += 1
                        else:
                            b -= 1
                            break
                    if not [a, min(b, now_b)].count(0):
                        able_info.append([a, min(b, now_b)])
                    a += 1
                else:
                    break

            for info in able_info:
                for a in range(1, info[0] + 1):
                    for b in range(1, info[1]+1):
                        h, nx, ny = 0, i, j
                        visited = [cafes[i][j]]
                        status = True
                        while status:
                            if h == 4:
                                if len(visited) > result:
                                    result = len(visited)
                                break

                            if h == 0 or h == 2:
                                for k in range(a):
                                    nx += di[h]
                                    ny += dj[h]
                                    if cafes[nx][ny] not in visited:
                                        visited.append(cafes[nx][ny])
                                    else:
                                        status = False
                                h += 1
                            elif h == 1:
                                for k in range(b):
                                    nx += di[h]
                                    ny += dj[h]
                                    if cafes[nx][ny] not in visited:
                                        visited.append(cafes[nx][ny])
                                    else:
                                        status = False
                                h += 1
                            elif h == 3:
                                for k in range(b - 1):
                                    nx += di[h]
                                    ny += dj[h]
                                    if cafes[nx][ny] not in visited:
                                        visited.append(cafes[nx][ny])
                                    else:
                                        status = False
                                h += 1

    if not result:
        result = -1
    print(f'#{tc} {result}')