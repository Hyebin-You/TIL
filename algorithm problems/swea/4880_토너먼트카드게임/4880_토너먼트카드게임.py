import sys
sys.stdin = open('sample_input.txt')


def RSF(a, b):
    if card_num[a] == card_num[b]:
        if a < b:
            return a
        else:
            return b
    elif (card_num[a], card_num[b]) in [(1, 3), (2, 1), (3, 2)]:
        return a
    else:
        return b


def tournament(i, j):
    if i == j:
        return i
    else:
        middle = (i + j) // 2
        a = tournament(i, middle)
        b = tournament(middle+1, j)
        return RSF(a, b)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_num = list(map(int, input().split()))

    print(f'#{tc} {tournament(0, N-1) + 1}')