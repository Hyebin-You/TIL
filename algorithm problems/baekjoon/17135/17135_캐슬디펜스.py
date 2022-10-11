from itertools import combinations as comb
from copy import deepcopy
import sys
input = sys.stdin.readline


def play_game(cc):
    arr = deepcopy(board)
    cnt = 0
    while True:
        attack_list = []
        for p in cc:
            able_attack = {k: [] for k in range(1, D+1)}
            for i in range(N-1, -1, -1):
                for j in range(M):
                    if arr[i][j] and abs(N - i) + abs(p - j) <= D:
                        able_attack[abs(N - i) + abs(p - j)].append((i, j))
            for v in able_attack.values():
                if len(v):
                    v.sort(key= lambda x:x[1])
                    if v[0] not in attack_list:
                        attack_list.append(v[0])
                    break
        for a in attack_list:
            arr[a[0]][a[1]] = 0
            cnt += 1

        arr = [[0] * M] + arr[:N-1]
        if sum([i.count(0) for i in arr]) == N*M:
            break

    return cnt


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0
for c in comb(range(M), 3):
    score = play_game(c)
    result = max(result, score)

print(result)

# 공격할 적들을 찾을 때 같은 적을 공격할 수 있다는 점을 유의할 것!