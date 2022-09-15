import sys
sys.stdin = open('sample_input.txt')


def make_tree(root):
    global num, tree

    if root <= N:
        make_tree(root*2)
        tree[root] = num
        num += 1
        make_tree(root*2+1)
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1

    make_tree(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')