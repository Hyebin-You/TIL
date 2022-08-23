def gcd(a, b):                              # 최대공약수를 구하는 함수
    for i in range(min(a,b), 0, -1):        # 둘 중 더 작은 수부터 1씩 줄여나가면서
        if a % i == 0 and b % i == 0:       # 최대공약수를 찾음
            return i


N, S = map(int, input().split())
pos = list(map(int, input().split()))
distance = [abs(pos[i] - S) for i in range(N)]  # 동생들과의 거리(절대값)

if N == 1:
    print(distance[0])                      # 동생이 한명이라면 찾을 필요 없이 그냥 거리 출력
else:
    for i in range(1, N):                   # 동생이 여러명이라면 동생들의 거리의 최대공약수 찾음
        distance[i] = gcd(distance[i-1], distance[i])
    print(distance[-1])

# 시간초과 발생