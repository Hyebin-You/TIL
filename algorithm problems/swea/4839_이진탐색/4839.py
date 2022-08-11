import sys

sys.stdin = open('sample_input.txt')


def binarySearch_times(book, key):
    start = 0
    end = len(book) - 1
    count = 0
    while start <= end:
        count += 1
        middle = (start + end)//2
        if book[middle] == key:
            break
        elif book[middle] > key:
            end = middle
        else:
            start = middle

    return count



T = int(input())

for tc in range(1, T+1):
    P, A, B, = map(int, input().split())
    book = [a for a in range(1, P+1)]

    num_A = binarySearch_times(book, A)
    num_B = binarySearch_times(book, B)

    if num_A < num_B:
        print(f'#{tc} A')
    elif num_B < num_A:
        print(f'#{tc} B')
    else:
        print(f'#{tc}', 0)