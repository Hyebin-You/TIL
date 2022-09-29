import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[] for _ in range(N+1)]

    for _ in range(E):
        a, b, w = map(int, input().split())
        arr[a].append((b, w))

    D = [0] * (N+1)
    q = [0]
    while q:
        n = q.pop(0)
        for i in arr[n]:
            if not D[i[0]] or D[i[0]] > D[n] + i[1]:
                D[i[0]] = D[n] + i[1]
                q.append(i[0])

    print(f'#{tc} {D[-1]}')