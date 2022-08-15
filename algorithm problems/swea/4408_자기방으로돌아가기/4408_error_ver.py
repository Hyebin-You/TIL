import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    moved = [0] * 200
    result = 0

    for i in range(N):
        for j in range(2):
            if arr[i][j] % 2:
                arr[i][j] = (arr[i][j] + 1)//2
            else:
                arr[i][j] //= 2

    for i in range(N):
        if moved[i] == 0:
            moved[i] = 1
            result += 1
            for j in range(i+1, N):
                if min(arr[i]) > max(arr[j]) or max(arr[i]) < min(arr[j]):
                    moved[j] = 1

    print(f'#{tc} {result}')


    # 처음 작성한 코드
    # 자신 이후에 자신과 겹치지 않는 경로를 찾도록 했으나 이후 경로들까지 겹치는 것을 체크하지 못함
    # 위에 언급한 오류에 대한 보완이 필요함