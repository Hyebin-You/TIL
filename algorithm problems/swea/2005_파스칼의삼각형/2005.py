import sys
sys.stdin = open('input.txt')


def P_tri(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        result = [0] * n
        prev = P_tri(n-1)
        for i in range(n):
            if i == 0 or i == n-1:
                result[i] = 1
            else:
                result[i] += prev[i-1] + prev[i]
        return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N+1):
        print(*P_tri(i))

