import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lines = list(input())
    result = 0
    cnt = 0

    for i in range(lines.index('1'), N):
        if lines[i] == '1':
            cnt += 1
        else:
            if result < cnt:
                result = cnt
                cnt = 0

    if result < cnt:
        result = cnt

    print(f'#{tc} {result}')