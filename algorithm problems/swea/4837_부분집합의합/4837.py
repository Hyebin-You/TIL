import sys

sys.stdin = open('sample_input.txt')


def subset_sum(subset):  # 부분 집합의 합을 구하는 함수
    result = 0
    for s in range(len(subset)):
        result += subset[s]
    return result


T = int(input())
A = [a for a in range(1, 13)]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    for i in range(1<<12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset.append(A[j])
            sums = subset_sum(subset)
        if len(subset) == N and sums == K:
            result += 1

    print(f'#{tc} {result}')