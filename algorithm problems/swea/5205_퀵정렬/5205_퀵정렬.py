import sys
sys.stdin = open('sample_input.txt')


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    p = arr[0]
    l, m, e = [], [], []
    for i in range(len(arr)):
        if arr[i] < p:
            l.append(arr[i])
        elif arr[i] > p:
            m.append(arr[i])
        else:
            e.append(arr[i])

    return quicksort(l) + e + quicksort(m)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nn = quicksort(nums)

    print(f'#{tc} {nn[N//2]}')