import sys
sys.stdin = open('sample_input.txt')


def after_time():
    global micro
    di = [0, -1, 1, 0, 0]  # 상, 하, 좌, 우
    dj = [0, 0, 0, -1, 1]
    d_change = {1: 2, 2: 1, 3: 4, 4: 3}

    for i in range(K):
        x, y = micro[i][0], micro[i][1]
        h = micro[i][3]
        if h:
            nx, ny = x + di[h], y + dj[h]
            if not nx or nx == N - 1 or not ny or ny == N - 1:  # 가장자리일때
                micro[i][2] //= 2
                if not micro[i][2]:  # 남은 미생물이 없다면
                    micro[i][0], micro[i][1] = 0, 0
                    micro[i][3] = 0
                else:
                    micro[i][3] = d_change[h]
            micro[i][0], micro[i][1] = nx, ny

    micro.sort()
    for i in range(K):          # 같은 위치에 있는 미생물 처리
        if micro[i][3]:
            idx = 1
            total = micro[i][2]
            h = [micro[i][3], micro[i][2]]
            while i + idx < K:
                if micro[i+idx][0] == micro[i][0] and micro[i+idx][1] == micro[i][1]:
                    total += micro[i+idx][2]
                    if h[1] < micro[i+idx][2]:
                        h[0], h[1] = micro[i+idx][3], micro[i+idx][2]
                    for j in range(4):
                        micro[i+idx][j] = 0
                    idx += 1
                else:
                    break
            micro[i][2], micro[i][3] = total, h[0]


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]
    # 저장된 값 [i, j, num, 방향]

    for time in range(M):
        after_time()

    result = 0
    for k in range(K):
        result += micro[k][2]

    print(f'#{tc} {result}')