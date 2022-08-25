import sys
sys.stdin = open('sample_input.txt')


def find_node_dist(s, g, ar):           # s : 출발 노드, g : 도착 노드, ar : 간선 정보 리스트
    visited = [0] * len(ar)
    q = [(s, 0)]
    while q:
        t = q.pop(0)
        visited[t[0]] = 1

        if arr[t[0]][g] == 1:
            return t[1] + 1
        else:
            for i in range(len(ar)):
                if arr[t[0]][i] == 1 and not visited[i] and (i, t[1] + 1) not in q:
                    q.append((i, t[1] + 1))

    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    line_nums = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]

    for line in line_nums:
        a, b = line
        arr[a][b] = arr[b][a] = 1

    print(f'#{tc} {find_node_dist(S, G, arr)}')