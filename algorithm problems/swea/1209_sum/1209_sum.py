import sys

sys.stdin = open('input.txt')

for tc in range(10):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = []
    for i in range(100):
        sum_1 = 0
        for j in range(100):
            sum_1 += arr[i][j]
        result.append(sum_1)

    for j in range(100):
        sum_2 = 0
        for i in range(100):
            sum_2 += arr[i][j]
        result.append(sum_2)

    sum_3 = 0
    sum_4 = 0
    for i in range(100):
        sum_3 += arr[i][i]
        sum_4 += arr[i][99-i]
    result.append(sum_3)
    result.append(sum_4)

    for i in range(len(result)-1, 0, -1):
        for j in range(i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j+1], result[j]

    print(f'#{n} {result[-1]}')