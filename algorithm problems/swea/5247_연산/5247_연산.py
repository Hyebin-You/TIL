import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    q = deque([N])
    status = True
    while q:
        n = q.popleft()
        nums = [n + 1, n - 1, n * 2, n - 10]
        for num in nums:
            if num == M:
                visited[num] = visited[n] + 1
                status = False
                break
            if 0 < num <= 1000000:
                if not visited[num]:
                    visited[num] = visited[n] + 1
                    q.append(num)
        if not status:
            break

    print(f'#{tc} {visited[M]}')