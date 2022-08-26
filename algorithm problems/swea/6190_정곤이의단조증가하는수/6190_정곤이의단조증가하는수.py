import sys
sys.stdin = open('s_input.txt')


def increase_num(num):
    num = str(num)
    for i in range(1, len(num)):
        if num[i-1] > num[i]:
            return False

    return True


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = -1
    for i in range(N):
        for j in range(i+1, N):
            n = arr[i] * arr[j]
            if increase_num(n):
                if n > result:
                    result = n

    print(f'#{tc} {result}')