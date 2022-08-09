import sys

sys.stdin = open('s_input.txt')

tc_num = int(input())

for tc in range(tc_num):
    N = int(input())

    lines = [0] * N
    for i in range(N):
        A, B = map(int, input().split())
        lines[i] = list(range(A, B + 1))

    P = int(input())
    result = []
    for i in range(P):
        C = int(input())
        count = 0
        for j in range(N):
            if C in lines[j]:
                count += 1
        result.append(count)

    result_p = ''
    for i in range(P):
        if i != P-1:
            result_p += str(result[i]) + ' '
        else:
            result_p += str(result[i])
    
    print(f'#{tc+1} {result_p}')