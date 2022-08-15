from collections import deque
import sys
input = sys.stdin.readline

result = 0
N = int(input())
limit_weight = list(map(int, input().split()))

M = int(input())
box_weight = list(map(int, input().split()))

limit_weight.sort(reverse=True)
box_weight.sort(reverse=True)

limit = deque(limit_weight)
box = deque(box_weight)

if limit[0] < box[0]:
    print(-1)
    sys.exit()
else:
    while True:
        for i in range(len(limit)):
            storage = deque()
            for j in range(len(box)):
                if limit[i] >= box[j]:
                    box.popleft()
                    break
                else:
                    storage.appendleft(box.popleft())
                    box.appendleft(0)
            for _ in range(box.count(0)):
                box.remove(0)
            box.extendleft(storage)

        result += 1
        if len(box) == 0:
            break

    print(result)

# 예제에 대해서 결과는 맞게 나오나 시간 초과...