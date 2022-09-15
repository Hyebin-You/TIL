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
            able_info = [0, 0]      # 현 좌표에서 최대 우상으로 몇번, 우하로 몇번 가능한지
            a, b = 1, 1
            while True:
                if 0 <= i + di[0]*a < N and 0 <= j + dj[0]*a < N:       # 우상 방향
                    a += 1
                else:
                    able_info[0] = a-1
                    break
            nx, ny = i + di[0]*(a-1), j + dj[0]*(a-1)
            while True:
                if 0 <= nx + di[1] * b < N and 0 <= ny + dj[1] * b < N:
                    b += 1
                else:
                    able_info[1] = b-1
                    break

            if able_info.count(0):
                continue
            for a in range(1, able_info[0]+1):      # 우상 방향 몇번
                for b in range(1, able_info[1]+1):      # 우하 방향 몇번
                    h, nx, ny = 0, i, j
                    visited = [cafes[i][j]]
                    status = True
                    while status:
                        if h == 4:
                            if len(visited) > result:
                                result = len(visited)
                                print(visited)
                            break

                        if h == 0 or h == 2:
                            for k in range(a):
                                nx += di[h]
                                ny += dj[h]
                                if cafes[nx][ny] not in visited:
                                    visited.append(cafes[nx][ny])
                                else: status = False
                            h += 1
                        elif h == 1:
                            for k in range(b):
                                nx += di[h]
                                ny += dj[h]
                                if cafes[nx][ny] not in visited:
                                    visited.append(cafes[nx][ny])
                                else: status = False
                            h += 1
                        elif h == 3:
                            for k in range(b-1):
                                nx += di[h]
                                ny += dj[h]
                                if cafes[nx][ny] not in visited:
                                    visited.append(cafes[nx][ny])
                                else: status = False
                            h += 1

    if not result:
        result = -1

    print(f'#{tc} {result}')