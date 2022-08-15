import sys
input = sys.stdin.readline

N, K = map(int, input().split())
j = [list(map(int, input().split())) for _ in range(N)]
weight = [int(input()) for _ in range(K)]
weight.sort()

j.sort(key=lambda i: i[1], reverse=True)
j.sort(key=lambda i: i[0])

result = 0
for i in range(K):
    max_value = 0
    for k in range(0, N):
        if weight[i] >= j[k][0]:
            if max_value < j[k][1]:
                max_value = j[k][1]
        else:
            break
    result += max_value
    weight[weight.index(max_value)] = 0

print(result)

# 시간 초과 발생.. heapq 방식으로 진행해야 한다고 함