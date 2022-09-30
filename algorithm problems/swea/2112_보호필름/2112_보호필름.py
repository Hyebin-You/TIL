import sys
sys.stdin = open('sample_input.txt')
from itertools import combinations


def test(arr):
    for i in range(W):
        cnt = 1
        status = arr[0][i]
        for j in range(1, D):
            if arr[j][i] == status:
                cnt += 1
            else:
                status = arr[j][i]
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            break
    else:
        return True

    return False


def put_in_and_test(arr, turn_list):
    turn_num = len(turn_list)
    q = [(arr, 0)]
    while q:
        ar, idx = q.pop(0)
        if idx == turn_num:
            if test(ar):
                return True
            continue

        nar = ar[:]
        nar[turn_list[idx]] = [0] * W
        q.append((nar, idx + 1))
        nar = ar[:]
        nar[turn_list[idx]] = [1] * W
        q.append((nar, idx + 1))

    return False


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    ff = [list(map(int, input().split())) for _ in range(D)]

    if put_in_and_test(ff, []):
        print(f'#{tc} {0}')
    else:
        result = 0
        for i in range(1, K+1):
            for c in combinations([k for k in range(D)], i):
                c_l = list(c)
                fff = ff[:]
                if put_in_and_test(fff, c_l):
                    result = i
                    break
            if result:
                break

        print(f'#{tc} {result}')