import sys
sys.stdin = open('input.txt')


def inorder(root):
    global result
    if root:
        inorder(c1[root])
        result.append(p[root])
        inorder(c2[root])


for tc in range(1, 11):
    N = int(input())
    p = [0] * (N+1)
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)

    for _ in range(N):
        P, char, left, right = 0, 0, 0, 0
        info = input().split()
        if len(info) != 4:
            info.extend([0] * (4 - len(info)))
        P, char, left, right = info
        p[int(P)] = char
        c1[int(P)] = int(left)
        c2[int(P)] = int(right)

    result = []
    inorder(1)
    print(f'#{tc}', ''.join(result))