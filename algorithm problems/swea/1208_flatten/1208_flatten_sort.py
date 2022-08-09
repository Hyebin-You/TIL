import sys

sys.stdin = open('input.txt')

for i in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for j in range(N):
        arr.sort()
        arr[0] += 1
        arr[-1] -= 1

    arr.sort()
    print(f'#{i} {arr[-1] - arr[0]}')