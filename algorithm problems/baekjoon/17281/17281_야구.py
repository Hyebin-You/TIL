from itertools import permutations as pp
import sys
input = sys.stdin.readline


def cal_score(arr):
    out_cnt = 0
    inning = 0
    now_p = 0
    b1, b2, b3 = 0, 0, 0
    score = 0
    while inning < N:
        info_inning = info[inning]
        if info_inning[arr[now_p]] == 1:
            score += b3
            b1, b2, b3 = 1, b1, b2
        elif info_inning[arr[now_p]] == 2:
            score += b2 + b3
            b1, b2, b3 = 0, 1, b1
        elif info_inning[arr[now_p]] == 3:
            score += b1 + b2 + b3
            b1, b2, b3 = 0, 0, 1
        elif info_inning[arr[now_p]] == 4:
            score += b1 + b2 + b3 + 1
            b1, b2, b3 = 0, 0, 0
        else:
            out_cnt += 1
        now_p += 1
        if now_p == 9:
            now_p = 0
        if out_cnt == 3:
            inning += 1
            out_cnt = 0
            b1, b2, b3 = 0, 0, 0

    return score


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

result = 0
for p in pp([1, 2, 3, 4, 5, 6, 7, 8], 8):
    p_list = list(p)[:3] + [0] + list(p)[3:]
    scores = cal_score(p_list)
    result = max(result, scores)

print(result)

# base를 리스트로 관리하면 시간초과 발생
# 개별 숫자로 관리하면 통과됨