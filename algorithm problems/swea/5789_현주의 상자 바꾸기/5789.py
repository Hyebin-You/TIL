import sys

sys.stdin = open('sample_input.txt')

tc_num = int(input())

for tc in range(tc_num):
    N, Q = map(int, input().split())
    boxs = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            boxs[j] = i + 1
    result = ''
    for i in range(N-1):
        result += str(boxs[i]) + ' '
    result += str(boxs[N-1])

    print(f'#{tc+1} {result}')