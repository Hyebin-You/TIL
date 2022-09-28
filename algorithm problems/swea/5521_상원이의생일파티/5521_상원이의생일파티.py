import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0] * (N + 1) for _ in range(N+1)]

    for i in info:
        arr[i[0]][i[1]] = 1
        arr[i[1]][i[0]] = 1

    invite = [0] * (N+1)
    q = [(1, 0)]
    while q:
        n, cnt = q.pop(0)
        if n not in invite:
            invite[n] = 1

            if cnt < 2:
                for i in range(1, N+1):
                    if arr[n][i] and not invite[i]:
                        q.append((i, cnt + 1))

    print(invite)
    print(f'#{tc} {sum(invite) - 1}')