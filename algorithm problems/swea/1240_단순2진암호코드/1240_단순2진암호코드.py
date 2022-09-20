import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    codes = [list(input()) for _ in range(N)]
    nums = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
            '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
            '0110111': 8, '0001011': 9
    }

    for i in range(N):
        a, b = 0, 0
        for j in range(M-1, 0, -1):
            if codes[i][j] == '1':
                a, b = i, j
                break
        if b:
            break

    code = codes[a][(b-56+1): b+1]
    i, idx = 0, 1
    result = [''] * 9
    while i < 56:
        result[idx] += code[i]
        i += 1
        if len(result[idx]) == 7:
            idx += 1

    num_odd, num_even = 0, 0
    for i in range(1, 9):
        if i % 2:
            num_odd += nums[result[i]]
        else:
            num_even += nums[result[i]]

    if (num_odd*3 + num_even) % 10:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {num_odd+num_even}')