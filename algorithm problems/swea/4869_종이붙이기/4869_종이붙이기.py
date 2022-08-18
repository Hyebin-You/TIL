import sys
import math
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = 0

    max_20 = N // 20
    for i in range(max_20 + 1):
        if N - 20 * i != 0:
            num_10 = (N - 20*i)//10
            nums = int(math.factorial(i + num_10)/(math.factorial(i)*math.factorial(num_10)))
            result += nums * (2**i)
        else:
            result += 2**i

    print(f'#{tc} {result}')