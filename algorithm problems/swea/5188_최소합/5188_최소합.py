import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0]     # 하, 우
    dj = [0, 1]

    result = 9*(N**2)
    stack = [(0, 0, arr[0][0])]
    while stack:
        x, y, num = stack.pop()
        for i in range(2):
            nx, ny = x + di[i], y + dj[i]
            if nx < N and ny < N:
                if (nx, ny) == (N-1, N-1):
                    if result > num + arr[nx][ny]:
                        result = num + arr[nx][ny]
                else:
                    stack.append((nx, ny, num + arr[nx][ny]))

    print(f'#{tc} {result}')