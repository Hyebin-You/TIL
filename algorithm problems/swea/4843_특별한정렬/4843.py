import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []

    for i in range(N - 1):
        minIdx = i
        for j in range(i+1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    for i in range(N//2):
        result.append(arr[-i-1])
        result.append(arr[i])

    if N%2 == 1:
        result.append(arr[N//2 + 1])

    print(f'#{tc}', *result[:10])