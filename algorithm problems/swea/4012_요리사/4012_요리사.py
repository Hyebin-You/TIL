import sys
sys.stdin = open('sample_input.txt')


def find_combination(idx, com1):
    global com_list
    if idx == N:
        if len(com1) == N//2:
            com_list.append(com1)
        return

    if len(com1) == N//2:
        com_list.append(com1)
        return

    find_combination(idx+1, com1)
    com2 = com1.copy()
    com2.append(idx)
    find_combination(idx+1, com2)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    com_list = []
    find_combination(0, [])

    result = 10**6
    for com in com_list:
        A = 0
        B = 0
        for i in range(len(com)):
            for j in range(len(com)):
                a, b = com[i], com[j]
                A += S[a][b]
        for i in range(N):
            if i not in com:
                for j in range(N):
                    if j not in com:
                        B += S[i][j]

        if abs(A-B) < result:
            result = abs(A-B)

    print(f'#{tc} {result}')