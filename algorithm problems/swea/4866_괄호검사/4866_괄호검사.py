import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    sentence = input()
    storage = []
    result = 1

    for s in sentence:
        if s == '(' or s == '{':
            storage.append(s)
        elif s == ')' or s == '}':
            if len(storage) == 0:
                result = 0
                break
            else:
                if s == ')' and storage.pop() != '(':
                    result = 0
                    break
                elif s == '}' and storage.pop() != '{':
                    result = 0
                    break

    if len(storage) != 0:
        result = 0

    print(f'#{tc} {result}')