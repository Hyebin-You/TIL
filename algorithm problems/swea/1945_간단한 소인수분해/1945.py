import sys

sys.stdin = open('input.txt')

N = int(input())

for tc in range(N):
    num = int(input())
    result = [0] * 5
    nums = [2, 3, 5, 7, 11]
    for i in range(5):
        while True:
            if num % nums[i]:
                break
            else:
                num //= nums[i]
                result[i] += 1

    print(f'#{tc+1} {result[0]} {result[1]} {result[2]} {result[3]} {result[4]}')