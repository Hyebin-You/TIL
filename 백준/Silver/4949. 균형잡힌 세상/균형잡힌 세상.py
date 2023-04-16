import sys
input = sys.stdin.readline

while True:
    line = list(input().rstrip())
    if line == ['.']:
        break

    stack = []
    result = 'no'
    for l in line:
        if l in ['(', '[']:
            stack.append(l)
        elif l == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                break
        elif l == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                break
    else:
        if not len(stack):
            result = 'yes'

    print(result)