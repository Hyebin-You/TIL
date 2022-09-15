import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * (N+1)
    tree[0] = -1

    for num in nums:
        idx = tree.index(0)
        tree[idx] = num
        while True:
            if tree[idx//2] > tree[idx]:
                tree[idx//2], tree[idx] = tree[idx], tree[idx//2]
                idx = idx//2
            else:
                break

    result = 0
    while N != 1:
        N //= 2
        result += tree[N]

    print(f'#{tc} {result}')