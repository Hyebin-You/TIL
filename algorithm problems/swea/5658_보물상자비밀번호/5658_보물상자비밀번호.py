import sys
sys.stdin = open('sample_input.txt')


def stot(num):
    sixteentoten = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    num = num[::-1]
    total = 0
    i = 0
    while i < len(num):
        if num[i] in sixteentoten.keys():
            total += sixteentoten[num[i]] * 16**i
        else:
            total += int(num[i]) * 16**i
        i += 1

    return total


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(input())

    num_list = [nums]
    for _ in range(N//4-1):
        l = num_list[-1]
        num_list.append([l[-1]] + l[:N-1])

    result = []
    for l in num_list:
        for i in range(4):
            k = N // 4
            result.append(''.join(l[k * i:k * i + k]))

    result = list(set(result))
    result.sort(reverse=True)
    fr = stot(result[K-1])
    print(f'#{tc} {fr}')