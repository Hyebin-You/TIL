import sys

sys.stdin = open('input.txt')

for i in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for j in range(N):
        for k in range(len(arr)-1, 0, -1):
            for l in range(k):
                if arr[l] > arr[l+1]:
                    arr[l], arr[l+1] = arr[l+1], arr[l]
        arr[0] += 1
        arr[-1] -= 1

    arr.sort()
    print(f'#{i} {arr[-1] - arr[0]}')

# sort 메서드 사용하지 않고 bubble sort 사용한 코드