import math


def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))


T = int(input())
for tc in range(T):
    N = int(input())
    num_2 = N // 2
    num_3 = N // 3
    storage = []      # 1, 2, 3의 개수를 담은 리스트

    for i in range(num_3 + 1):
        num = N - 3 * i
        for j in range(num_2+1):
            if num - 2 * j >= 0:
                storage.append([num - 2 * j, j, i])

    result = 0
    for info in storage:
        if info.count(0) == 2:
            result += 1
        elif info.count(0) == 1:
            idx = info.index(0)
            info.pop(idx)
            a, b = info[0], info[1]
            result += nCr(a+b, a)
        else:
            a, b, c = info[0], info[1], info[2]
            result += nCr(a+b+c, a) * nCr(b+c, c)

    print(result)