import sys
sys.stdin = open('input.txt')

for a in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]

    b = 100  # 회문이 될 수 있는 최대 길이
    result = -1 # 반복문 탈출과 관련된 초기값
    while b > 0:
        # 가로탐색
        for i in range(100):
            for j in range(100 - b + 1):
                word = arr[i][j:j+b]
                if word == word[::-1]:
                    result = b
                    break
            if result != -1:
                break
        else:  # 세로탐색
            for k in range(100):
                for h in range(100 - b + 1):
                    word = ''
                    for l in range(b):
                        word += arr[h+l][k]
                    if word == word[::-1]:
                        result = b
                        break
                if result != -1:
                    break

        if result != -1:
            break

        b -= 1

    print(f'#{tc} {result}')