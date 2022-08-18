import sys
sys.stdin = open('input.txt')


def find_way(start):
    visited[start] = 1
    if start == 99:
        return 1

    for next in range(1, 100):
        if ways[start][next] == 1 and visited[next] == 0:
            if find_way(next) == 1:  # 이 조건문 안넣으면 0 만 리턴함
                return 1
    else:
        return 0


for _ in range(10):
    tc, N = map(int, input().split())
    data = list(map(int, input().split()))
    ways = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0] * 100

    for i in range(N):
        ways[data[i*2]][data[i*2 + 1]] = 1

    print(f'#{tc} {find_way(0)}')