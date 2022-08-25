import sys
sys.stdin = open('sample_input.txt')


def last_pizza(n, arr):          # n : 화덕 크기, arr : 피자 정보가 저장된 리스트
    storage = [arr[i] for i in range(n)]
    p_n = len(arr)
    z_cnt = 0

    i = n
    while z_cnt != p_n - 1:
        t = storage.pop(0)
        if not t[0]:
            if t[1]:
                z_cnt += 1
            if i < p_n:
                storage.append((arr[i][0]//2, arr[i][1]))
                i += 1
            else:
                storage.append((0, 0))
        else:
            storage.append((t[0]//2, t[1]))

    for j in range(len(storage)):
        if storage[j][1] != 0:
            return storage[j][1]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        pizza.append((cheese[i], i+1))

    print(f'#{tc} {last_pizza(N, pizza)}')