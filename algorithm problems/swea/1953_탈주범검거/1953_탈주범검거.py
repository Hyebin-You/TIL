import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())           # 맨홀뚜껑 위치 (R, C)
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]             # 상 하 좌 우
    dj = [0, 0, -1, 1]
    structure = {1:[0, 1, 2, 3], 2:[0, 1], 3:[2, 3], 4:[0, 3], 5:[1, 3], 6:[1, 2], 7:[0, 2]}

    able_pos = [[] for _ in range(L+1)]
    able_pos[1].append((R, C))
    visited = [(R, C)]
    for time in range(1, L):
        pos = able_pos[time]
        for i in range(len(pos)):
            a, b = pos[i]
            for h in structure[tunnel[a][b]]:
                if 0 <= a + di[h] < N and 0 <= b + dj[h] < M:
                    if (a + di[h], b + dj[h]) not in visited:
                        t = tunnel[a + di[h]][b + dj[h]]
                        if not t:
                            continue
                        if not h and 1 in structure[t]:
                            able_pos[time + 1].append((a + di[h], b + dj[h]))
                            visited.append((a + di[h], b + dj[h]))
                        elif h == 1 and 0 in structure[t]:
                            able_pos[time + 1].append((a + di[h], b + dj[h]))
                            visited.append((a + di[h], b + dj[h]))
                        elif h == 2 and 3 in structure[t]:
                            able_pos[time + 1].append((a + di[h], b + dj[h]))
                            visited.append((a + di[h], b + dj[h]))
                        elif h == 3 and 2 in structure[t]:
                            able_pos[time + 1].append((a + di[h], b + dj[h]))
                            visited.append((a + di[h], b + dj[h]))

    print(f'#{tc} {len(visited)}')