import sys
sys.stdin = open('sample_input.txt')


def row_test(ar):
    if ar.count(ar[0]) == len(ar):      # 높이 차이가 없는 경우
        return True

    # 높이 차이가 있을때
    pos = [0] * N
    for i in range(N-1):
        if ar[i] != ar[i+1]:
            if abs(ar[i] - ar[i+1]) == 1:
                if ar[i] < ar[i+1]:
                    s = i           # 판단 기준점(낮은 곳으로)
                    for j in range(X):
                        if 0 <= s - j and ar[s-j] == ar[s] and not pos[s-j]:
                            pos[s-j] = 1
                        else:
                            return False
                else:
                    s = i + 1
                    for j in range(X):
                        if s + j < N and ar[s+j] == ar[s] and not pos[s+j]:
                            pos[s+j] = 1
                        else:
                            return False
            else:
                return False
    else:
        return True


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        a = arr[i].copy()
        b = [arr[j][i] for j in range(N)]
        if row_test(a):
            result += 1
        if row_test(b):
            result += 1

    print(f'#{tc} {result}')