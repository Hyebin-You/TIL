import sys
from pprint import pprint
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, s = map(int, input().split())
    info = list(map(int, input().split()))
    arr = [[0] * 101 for _ in range(101)]

    for i in range(N//2):
        f, t = info[i*2], info[i*2+1]
        arr[f][t] = 1

    result = [[s]]
    visited = [0] * 101
    visited[s] = 1

    while True:
        start = result[-1]
        receive = []
        for i in range(len(start)):
            for j in range(101):
                if arr[start[i]][j] and not visited[j]:
                    receive.append(j)
                    visited[j] = 1

        if not len(receive):
            break
        else:
            result.append(receive)

    print(f'#{tc} {max(result[-1])}')