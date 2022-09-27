import sys
sys.stdin = open('sample_input.txt')


def binarysearch(arr, n, start, end):
    if start == end:
        if arr[start] == n:
            return True
        else:
            return False

    status = 0
    while start <= end:
        m = (start + end)//2
        if n < arr[m]:
            if not status or status == 2:
                end = m - 1
                status = 1
            else:
                return False
        elif n > arr[m]:
            if not status or status == 1:
                start = m + 1
                status = 2
            else:
                return False
        else:
            return True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums1.sort()
    nums2 = list(map(int, input().split()))

    result = 0
    for num in nums2:
        if binarysearch(nums1, num, 0, N-1):
            result += 1

    print(f'#{tc} {result}')