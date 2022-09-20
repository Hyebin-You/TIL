import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    result = ''
    i = 1
    while True:
        if 2**(-i) <= N:
            result += '1'
            N -= 2**(-i)
            i += 1
        elif 2**(-i) > N:
            result += '0'
            i += 1

        if not N:
            break

        if i == 13:
            result = 'overflow'
            break

    print(f'#{tc} {result}')