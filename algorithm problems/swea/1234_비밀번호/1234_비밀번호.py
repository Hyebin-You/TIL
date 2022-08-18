import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, Pa = input().split()
    N = int(N)
    result = []
    top = -1

    for i in range(N):
        if top == -1:
            result.append(Pa[i])
            top += 1
        else:
            if result[top] == Pa[i]:
                result.pop()
                top -= 1
            else:
                result.append(Pa[i])
                top += 1

    print(f'#{tc}', ''.join(result))