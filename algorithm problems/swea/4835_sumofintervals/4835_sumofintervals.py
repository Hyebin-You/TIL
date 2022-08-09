import sys

sys.stdin = open('sample_input.txt')

tc_num = int(input())

for tc in range(tc_num):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sums = [0] * (N - M + 1)

    for i in range(N - M + 1):
        for j in range(M):
            sums[i] += nums[i + j]

    for i in range(len(sums)-1, 0, -1):
        for j in range(i):
            if sums[j] > sums[j+1]:
                sums[j], sums[j+1] = sums[j+1], sums[j]

    print(f'#{tc+1} {sums[-1] - sums[0]}')