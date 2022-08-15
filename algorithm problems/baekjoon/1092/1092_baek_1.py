import sys
input = sys.stdin.readline

N = int(input())
limit_weight = list(map(int, input().split()))

M = int(input())
box_weight = list(map(int, input().split()))
result = 0

limit_weight.sort()
box_weight.sort()

if limit_weight[-1] < box_weight[-1]:
    result = -1
else:
    while True:
        for i in range(N-1, -1, -1):
            storage = []
            for j in range(len(box_weight)-1, -1, -1):
                if limit_weight[i] >= box_weight[j]:
                    box_weight.pop()
                    break
                else:
                    storage.append(box_weight.pop())
            box_weight += storage
            box_weight.sort()

        if len(box_weight) == 0:
            result += 1
            break
        else:
            result += 1

print(result)

#시간 초과....