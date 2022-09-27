import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    stack = []
    result = 0
    for i in range(N):
        stack.append((1, arr[0][i], [i]))
        result += arr[i][i]

    while stack:
        l_idx, total, visited = stack.pop()
        if l_idx == N:
            if total < result:
                result = total
            continue
        for i in range(N):
            if i not in visited and total + arr[l_idx][i] < result:
                stack.append((l_idx+1, total + arr[l_idx][i], visited + [i]))

    print(f'#{tc} {result}')