import sys

sys.stdin = open('sample_input.txt')

N = int(input())

for tc in range(N):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc+1} {arr[-1] - arr[0]}')