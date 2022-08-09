import sys

sys.stdin = open('sample_input.txt')

N = int(input())

for tc in range(N):
    n = int(input())
    cards = input()
    count_n = [0] * 10

    for i in range(n):
        count_n[int(cards[i])] += 1

    max_n = 0
    num = 0
    for i in range(10):
        if max_n < count_n[i]:
            max_n = count_n[i]
            num = i
        elif max_n == count_n[i]:
            num = i

    print(f'#{tc + 1} {num} {max_n}')