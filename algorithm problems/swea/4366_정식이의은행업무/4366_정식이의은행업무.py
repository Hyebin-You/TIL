import sys
sys.stdin = open('sample_input.txt')


def two_ten(num):           # 이진수를 십진수 숫자로 바꾸는 함수
    l = len(num)
    result = 0
    for i in range(l):
        result += int(num[i]) * 2**(l-i-1)
    return result


def three_ten(num):
    l = len(num)
    result = 0
    for i in range(l):
        result += int(num[i]) * 3**(l-i-1)
    return result


T = int(input())
for tc in range(1, T+1):
    num2 = list(input())
    num3 = list(input())

    num2_set = {two_ten(num2)}
    num3_set = {three_ten(num3)}

    for i in range(len(num2)):
        n = num2[i]
        for j in range(2):
            if int(n) != j:
                num2[i] = j
                num2_set.add(two_ten(num2))
                num2[i] = n

    for i in range(len(num3)):
        n = num3[i]
        for j in range(3):
            if int(n) != j:
                num3[i] = j
                num3_set.add(three_ten(num3))
        num3[i] = n

    result = num2_set & num3_set
    print(f'#{tc}', *result)