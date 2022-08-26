import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    if len(farm) == 1:
        print(f'#{tc} {farm[0][0]}')
    else:
        result = farm[0][N // 2] + farm[-1][N // 2]
        result += sum(farm[N // 2])

        for i in range(1, N // 2):
            result += farm[i][N // 2] + farm[-i - 1][N // 2]
            for j in range(1, i + 1):
                result += farm[i][N // 2 + j] + farm[i][N // 2 - j]
                result += farm[-i - 1][N // 2 + j] + farm[-i - 1][N // 2 - j]

        print(f'#{tc} {result}')
