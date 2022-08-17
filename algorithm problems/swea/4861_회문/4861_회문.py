import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 가로 탐색
    result = 0
    for i in range(N):
        for j in range(N-M+1):
            a = arr[i][j:j+M]
            b = a[::-1]
            if a == b:
                result = a
        if result != 0:
            break
    else:  # 세로 탐색
        for k in range(N):
            for h in range(N-M+1):
                a = ''
                for l in range(M):
                    a += arr[h+l][k]
                if a == a[::-1]:
                    result = a
            if result != 0:
                break

    print(f'#{tc} {result}')