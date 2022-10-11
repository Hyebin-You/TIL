import sys
from collections import deque
input = sys.stdin.readline


def near(arr):
    q = deque([arr[0]])
    check = []

    while q:
        s = q.popleft()
        if s not in check:
            check.append(s)
        for v in near_info[s]:
            if v in arr and v not in check:
                q.append(v)

    check.sort()
    if check == arr:
        return True
    else:
        return False


def d_n(a1, a2):
    sum_1 = sum([p_n[x] for x in a1])
    sum_2 = sum([p_n[x] for x in a2])
    return abs(sum_2 - sum_1)


N = int(input())
p_n = list(map(int, input().split()))
near_info = {}
for i in range(N):
    info = list(map(int, input().split()))
    near_info[i] = [x - 1 for x in info[1:]]

result = 10**8
stack = [([], [], 0)]
while stack:
    v1, v2, idx = stack.pop()
    if idx == N:
        if len(v1) and len(v2):
            if near(v1) and near(v2):
                a = d_n(v1, v2)
                result = min(result, a)
        continue

    stack.append((v1 + [idx], v2, idx + 1))
    stack.append((v1, v2 + [idx], idx + 1))

if result == 10**8:
    result = -1

print(result)