import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    sentence = input()

    # isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    # icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}

    stack = []
    result = ''

    for char in sentence:
        if char in '+*()':
            if not stack:
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char in '*':
                while stack and stack[-1] in '*':
                    result += stack.pop()
                stack.append(char)
            elif char in '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += char

    while stack:
        result += stack.pop()

    for char in result:
        if char in '*+':
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(a+b)
            elif char == '*':
                stack.append(a*b)
        else:
            stack.append(int(char))

    print(f'#{tc} {stack[0]}')