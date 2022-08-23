import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    sentence = input()
    postfix = []
    stack = []
    num = {'+': 1, '*': 2}

    for i in range(len(sentence)):
        if sentence[i] != '+' and sentence[i] != '*':
            postfix.append(int(sentence[i]))
        else:
            if len(stack):
                prev = stack[-1]
                if num[sentence[i]] > num[prev]:
                    stack.append(sentence[i])
                else:
                    while True:
                        a = stack.pop()
                        postfix.append(a)
                        if not len(stack):
                            stack.append(sentence[i])
                            break
                        elif num[sentence[i]] > num[stack[-1]]:
                            stack.append(sentence[i])
                            break
            else:
                stack.append(sentence[i])
    else:
        for _ in range(len(stack)):
            postfix.append(stack.pop())

    for i in range(len(postfix)):
        if postfix[i] != '*' and postfix[i] != '+':
            stack.append(postfix[i])
        else:
            a = stack.pop()
            b = stack.pop()
            if postfix[i] == '+':
                stack.append(a+b)
            else:
                stack.append(a*b)

    print(f'#{tc} {stack[0]}')