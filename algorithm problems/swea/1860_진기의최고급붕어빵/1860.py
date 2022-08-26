import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time_list = list(map(int, input().split()))

    time_list.sort()
    for i in range(N):
        bb = K * (time_list[i] // M) - i        # 빵의 개수는 생산한거 - 내 앞의 손님이 가져간 거
        if bb <= 0:
            result = 'Impossible'
            break
    else:
        result = 'Possible'

    print(f'#{tc} {result}')