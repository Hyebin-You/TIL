import sys
sys.stdin = open('sample_input.txt')


def find_max(ar, m):
    l = len(ar)
    total = 0
    stack = [(0, ar[0], [ar[0]]), (0, 0, [])]
    while stack:
        s, w, n_l = stack.pop()
        s += 1
        if s == l:
            if w <= m:
                k = [h**2 for h in n_l]
                if sum(k) > total:
                    total = sum(k)
        else:
            stack.append((s, w, n_l))
            n_ll = n_l + [ar[s]]
            stack.append((s, w + ar[s], n_ll))

    return total


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    h_info = []

    honey_info = []
    for i in range(N):
        for j in range(N-M+1):
            a = arr[i][j:j+M]
            h_info.append((find_max(a, C), (i, j)))

    h_info.sort()

    result = 0
    for i in range(len(h_info)):
        t = h_info[i][0]
        n_pos = [(h_info[i][1][0], h_info[i][1][1] + k) for k in range(M)]
        for j in range(len(h_info)):
            if i == j:
                continue
            n_j_pos = [(h_info[j][1][0], h_info[j][1][1] + k) for k in range(M)]
            if h_info[j][1] not in n_pos and h_info[i][1] not in n_j_pos:
                if t + h_info[j][0] > result:
                    result = t + h_info[j][0]

    print(f'#{tc} {result}')