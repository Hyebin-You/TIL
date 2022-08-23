N, S = map(int, input().split())
pos = list(map(int, input().split()))

for i in range(N):
    pos[i] = abs(pos[i]-S)


def euclidean(a, b):                    # 유클리드 호제법 함수
    if a > b:
        if a % b == 0:
            return b
        else:
            return euclidean(a%b, b)
    else:
        if b % a == 0:
            return a
        else:
            return euclidean(a, b%a)


if len(pos) == 1:
    print(pos[0])
else:
    stack = [pos[0]]
    for i in range(1, N):
        prev = stack.pop()
        stack.append(euclidean(prev, pos[i]))
    print(stack[0])



'''
유클리드 호제법 다르게 구현한 함수
def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

x가 y보다 큰 수여야 한다.
'''