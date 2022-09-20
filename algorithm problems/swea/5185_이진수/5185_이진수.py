import sys
sys.stdin = open('sample_input.txt')


def ten_two(num):
    num2 = ''

    while True:
        if num//2:
            num2 += str(num%2)
            num //= 2
        else:
            num2 +=str(num)
            break

    if len(num2) != 4:
        num2 += '0' * (4 - len(num2))

    return num2[::-1]


T = int(input())
for tc in range(1, T+1):
    N, num16 = input().split()
    result = ''

    num16_10 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(int(N)):
        if num16[i].isnumeric():
            result += ten_two(int(num16[i]))
        else:
            result += ten_two(num16_10[num16[i]])

    print(f'#{tc} {result}')