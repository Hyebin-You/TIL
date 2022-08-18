import sys
sys.stdin = open('sample_input.txt')


def find_way(start):
    visited[start] = 1
    if start == G:
        return 1

    for next in range(1, V+1):
        if ways[start][next] == 1 and visited[next] == 0:
            if find_way(next) == 1:  # 이 조건문 안넣으면 0 만 리턴함
                return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    visited = [0] * (V+1)

    ways = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for way in data:
        ways[way[0]][way[1]] = 1

    print(f'#{tc} {find_way(S)}')