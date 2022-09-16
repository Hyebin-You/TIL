import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    house = []

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                house.append((i, j))

    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(2*N-1, 0, -1):
                cost = k**2 + (k-1)**2
                h_cnt = 0
                for h in house:
                    if abs(h[0] - i) + abs(h[1] - j) < k:
                        h_cnt += 1
                if h_cnt * M >= cost:
                    if result < h_cnt:
                        result = h_cnt

    print(f'#{tc} {result}')