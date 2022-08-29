import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if i == 0 or not arr[i-1][j]:
                    k = 1
                    cnt = 1
                    while True:
                        if i + k < N and arr[i+k][j]:
                            cnt += 1
                            k += 1
                        else:
                            break
                    if cnt > result:
                        result = cnt
                if j == 0 or not arr[i][j-1]:
                    k = 1
                    cnt = 1
                    while True:
                        if j + k < M and arr[i][j+k]:
                            cnt += 1
                            k += 1
                        else:
                            break
                    if cnt > result:
                        result = cnt

    print(f'#{tc} {result}')