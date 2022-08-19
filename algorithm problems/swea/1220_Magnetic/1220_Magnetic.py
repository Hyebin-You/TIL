import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        stack = []
        top = -1
        for j in range(N):
            if arr[j][i] != 0:
                if top == -1:
                    stack.append(arr[j][i])
                    top += 1
                else:
                    prev = stack.pop()
                    top -= 1
                    if prev == arr[j][i]:
                        stack.append(prev)
                        top += 1
                    else:
                        stack.append(prev)
                        stack.append(arr[j][i])
                        top += 2
        if stack[0] == 2:
            stack.pop(0)
        if stack[-1] == 1:
            stack.pop()

        result += len(stack)//2

    print(f'#{tc} {result}')