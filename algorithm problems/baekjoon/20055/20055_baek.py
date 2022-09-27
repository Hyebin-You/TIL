import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = [0] * N

result = 0
while True:
    # 벨트와 로봇 회전
    belt = [belt[-1]] + belt[:2*N-1]
    robots = [0] + robots[0:N-2] + [0]

    # 로봇 이동
    for i in range(N-2, 0, -1):
        if robots[i]:
            if belt[i+1] and not robots[i + 1]:
                robots[i], robots[i + 1] = robots[i + 1], robots[i]
                belt[i+1] -= 1

    robots[N-1] = 0

    # 올리는 위치 로봇 올리기
    if belt[0]:
        robots[0] = 1
        belt[0] -= 1

    result += 1

    if belt.count(0) >= K:
        break

print(result)