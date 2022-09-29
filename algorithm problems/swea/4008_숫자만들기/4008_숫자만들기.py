import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    q = deque([(0, nums[0], operator)])
    result = []
    while q:
        idx, n, op = q.popleft()
        if idx == N-1:
            result.append(n)
            continue

        if op[0]:
            opp = op[:]
            opp[0] -= 1
            q.append((idx + 1, n + nums[idx+1], opp))
        if op[1]:
            opp = op[:]
            opp[1] -= 1
            q.append((idx + 1, n - nums[idx + 1], opp))
        if op[2]:
            opp = op[:]
            opp[2] -= 1
            q.append((idx + 1, n * nums[idx + 1], opp))
        if op[3]:
            opp = op[:]
            opp[3] -= 1
            if n < 0:
                w = -(-n//nums[idx+1])
            else:
                w = n//nums[idx+1]
            q.append((idx + 1, w, opp))

    print(f'#{tc} {max(result) - min(result)}')

    # deque 안하고 그냥 리스트 사용하면 시간초과 발생
    # 그냥 리스트로도 시간 초과 안나도록 해볼것것