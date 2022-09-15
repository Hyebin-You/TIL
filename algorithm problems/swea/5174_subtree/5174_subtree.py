import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lines = list(map(int, input().split()))

    c1 = [0] * (E+2)
    c2 = [0] * (E+2)
    for i in range(E):
        p, c = lines[2*i], lines[2*i + 1]
        if not c1[p]:
            c1[p] = c
        else:
            c2[p] = c

    stack = [N]
    result = []
    while stack:
        root = stack.pop()
        result.append(root)
        if c1[root]:
            stack.append(c1[root])
        if c2[root]:
            stack.append(c2[root])

    print(f'#{tc} {len(result)}')