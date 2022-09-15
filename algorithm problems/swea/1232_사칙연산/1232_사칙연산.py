import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    info = [list(input().split()) for _ in range(N)]
    tree = [0] * (N+1)

    for i in info:
        tree[int(i[0])] = i[1]

    for i in range(N, 0, -1):
        if not tree[i].isdecimal():
            a, b = int(info[i-1][2]), int(info[i-1][3])
            if tree[i] == '+':
                tree[i] = int(tree[a]) + int(tree[b])
            elif tree[i] == '-':
                tree[i] = int(tree[a]) - int(tree[b])
            elif tree[i] == '*':
                tree[i] = int(tree[a]) * int(tree[b])
            else:
                tree[i] = int(tree[a]) // int(tree[b])

    print(f'#{tc} {tree[1]}')