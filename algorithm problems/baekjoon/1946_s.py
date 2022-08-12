import sys
input=sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [0] * N
    count = 0

    for i in range(N):
        arr[i] = list(map(int, input().split()))
    
    arr.sort()
    min_n = arr[0][1]
    for j in range(N):
        if arr[j][1] <= min_n:
            count += 1
            min_n = arr[j][1]

    print(count)

#얘는 위에 input 바꾸니까 성공