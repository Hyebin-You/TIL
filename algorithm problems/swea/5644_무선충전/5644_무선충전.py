import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    A_move = [0] + list(map(int, input().split()))
    B_move = [0] + list(map(int, input().split()))
    BCs = [list(map(int, input().split())) for _ in range(A)]

    dx = [0, 0, 1, 0, -1]         # 상 1 우 2 하 3 좌 4
    dy = [0, -1, 0, 1, 0]
    ax, ay = 1, 1
    bx, by = 10, 10

    result = 0
    for i in range(M+1):
        ax, ay = ax + dx[A_move[i]], ay + dy[A_move[i]]
        bx, by = bx + dx[B_move[i]], by + dy[B_move[i]]
        A_BC = []
        B_BC = []
        for BC in BCs:
            if abs(ax - BC[0]) + abs(ay - BC[1]) <= BC[2]:
                A_BC.append(BC)
            if abs(bx - BC[0]) + abs(by - BC[1]) <= BC[2]:
                B_BC.append(BC)
        total = 0
        if len(A_BC) and len(B_BC):
            for ab in A_BC:
                for bb in B_BC:
                    if ab == bb:
                        if total < ab[3]:
                            total = ab[3]
                    else:
                        if total < ab[3] + bb[3]:
                            total = ab[3] + bb[3]
        elif len(A_BC):
            total = max(i[3] for i in A_BC)
        elif len(B_BC):
            total = max(i[3] for i in B_BC)

        result += total

    print(f'#{tc} {result}')