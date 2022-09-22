import sys
from itertools import permutations as pp
sys.stdin = open('sample_input.txt')


def find_min():
    global result

    for p in pp([i for i in range(1, N)]):
        s = 0
        total = 0
        for i in p:
            total += info[s][i]
            s = i
        total += info[i][0]
        if result > total:
            result = total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    result = 10**9
    find_min()
    print(f'#{tc} {result}')