import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    info.sort()
    info.sort(key=lambda x: x[1])

    e = info[0][1]
    cnt = 1
    for i in range(1, N):
        if info[i][0] >= e:
            cnt += 1
            e = info[i][1]

    print(f'#{tc} {cnt}')