import sys

sys.stdin = open('sample_input.txt')

N = int(input())

for tc in range(N):
    # K는 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N은 종점 번호
    # M은 충전기가 설치된 M개의 정류장 번호
    K, N, M = map(int, input().split())
    # station은 충전기가 설치된 정류장 번호들
    station = list(map(int, input().split()))
    position = 0
    counts = 0

    while True:
        if position + K >= N:
            break

        non_counts = 0
        for i in range(K, 0, -1):
            if (position + i) in station:
                counts += 1
                position += i
                break
            else:
                non_counts += 1
        if non_counts == K:
            counts = 0
            break

    print(f'#{tc + 1} {counts}')