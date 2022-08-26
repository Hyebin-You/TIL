import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    result = 0

    # 가로 회문 판별
    for i in range(8):
        for j in range(9-N):
            word = arr[i][j:j+N]
            if word == word[::-1]:
                result += 1

    # 세로 회문 판별
    for i in range(8):
        for j in range(9-N):
            word = ''
            for k in range(N):
                word += arr[j+k][i]
            if word == word[::-1]:
                result += 1

    print(f'#{tc} {result}')