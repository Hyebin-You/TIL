import sys
input = sys.stdin.readline

N = int(input())
limit_weight = list(map(int, input().split()))

M = int(input())
box_weight = list(map(int, input().split()))

limit_weight.sort(reverse=True)
box_weight.sort(reverse=True)

result = 0
if box_weight[0] > limit_weight[0]:
    print(-1)
    sys.exit()

while len(box_weight) > 0:
    for i in range(len(limit_weight)):
        for j in range(len(box_weight)):
            if limit_weight[i] >= box_weight[j]:
                del box_weight[j]
                break

    result += 1

print(result)

# 시간 초과... pypy로 하니 통과됨...