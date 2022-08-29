import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    change_cnt = []
    for line in flag:
        w_cnt = M - line.count('W')     # 흰줄로 할때 바꿔야 하는 개수
        b_cnt = M - line.count('B')
        r_cnt = M - line.count('R')
        change_cnt.append((w_cnt, b_cnt, r_cnt))

    min_cnt = N*M
    for w in range(0, N-2):    # 위에 흰줄 최소 0개에서 최대 N-3개
        for b in range(1, N - 1 - w):  # 중간 파란줄 최소 1개에서 최대 N-2-i개
            cnt = 0
            r = N - 2 - w - b
            for i in range(w):
                cnt += change_cnt[1+i][0]
            for i in range(b):
                cnt += change_cnt[1+w+i][1]
            for i in range(r):
                cnt += change_cnt[1+w+b+i][2]
            if cnt < min_cnt:
                min_cnt = cnt

    min_cnt += change_cnt[0][0] + change_cnt[-1][2]
    print(f'#{tc} {min_cnt}')